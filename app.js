/* ============================
   PyLearn - Application Logic
   ============================ */

(function () {
  'use strict';

  // ===== CONSTANTS =====
  const STORAGE = {
    PASSWORD: 'pylearn_password',
    PROGRESS: 'pylearn_progress',
  };
  // SHA-256 hash of 'jack1234@@'
  const DEFAULT_PW_HASH = '28d1b7626bc9b7ee36b2d3f9e1ed9aa78faa54c0191a8b56d9efa2b63fcae6de';

  // ===== STATE =====
  const state = {
    mode: 'student',
    authenticated: false,
    categories: [],
    currentCatIndex: 0,
    currentLesIndex: 0,
    completed: new Set(),
    pyodide: null,
    pyodideReady: false,
    editor: null,
    isPreview: false,
    teacherMenuOpen: false,
    editingTestCases: [],
    currentTcIndex: 0,
  };

  // ===== DOM HELPERS =====
  const $ = (id) => document.getElementById(id);
  const show = (el) => { if (typeof el === 'string') el = $(el); el?.classList.remove('hidden'); };
  const hide = (el) => { if (typeof el === 'string') el = $(el); el?.classList.add('hidden'); };

  // ===== UTILITY =====
  async function sha256(text) {
    const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
    return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
  }

  function getStoredHash() {
    return localStorage.getItem(STORAGE.PASSWORD) || DEFAULT_PW_HASH;
  }

  function toast(msg, type = '') {
    const t = $('toast');
    t.textContent = msg;
    t.className = 'toast ' + type;
    show(t);
    setTimeout(() => hide(t), 2800);
  }

  // ===== CUSTOM DIALOGS =====
  let promptResolve = null;
  function appPrompt(message, defaultVal = '') {
    return new Promise(resolve => {
      promptResolve = resolve;
      $('prompt-message').textContent = message;
      $('prompt-input').value = defaultVal;
      show('prompt-modal');
      setTimeout(() => $('prompt-input').focus(), 50);
    });
  }
  function closePrompt(val = null) {
    hide('prompt-modal');
    if (promptResolve) { promptResolve(val); promptResolve = null; }
  }

  let confirmResolve = null;
  function appConfirm(message) {
    return new Promise(resolve => {
      confirmResolve = resolve;
      $('confirm-message').textContent = message;
      show('confirm-modal');
    });
  }
  function closeConfirm(val = false) {
    hide('confirm-modal');
    if (confirmResolve) { confirmResolve(val); confirmResolve = null; }
  }

  // ===== PYODIDE =====
  async function initPyodide() {
    try {
      state.pyodide = await loadPyodide();
      state.pyodide.runPython(`
import sys, io
import builtins
from js import prompt as _js_prompt

_is_automated_test = False
_automated_inputs = []

def _custom_input(p=""):
    global _automated_inputs, _is_automated_test
    if _is_automated_test:
        if len(_automated_inputs) > 0:
            return str(_automated_inputs.pop(0))
        return ""
    r = _js_prompt(str(p))
    return r if r is not None else ""

builtins.input = _custom_input
`);
      state.pyodideReady = true;
      const badge = $('pyodide-status');
      badge.classList.remove('loading');
      badge.classList.add('ready');
      badge.querySelector('.status-text').textContent = 'Python 준비 완료';
      $('btn-run').disabled = false;
    } catch (e) {
      console.error('Pyodide load failed:', e);
      const badge = $('pyodide-status');
      badge.querySelector('.status-text').textContent = 'Python 로드 실패';
    }
  }

  async function runPython(code, testInput = null) {
    if (!state.pyodideReady) return { output: '', error: 'Python이 아직 로딩 중입니다...' };
    try {
      state.pyodide.runPython('sys.stdout = io.StringIO()\nsys.stderr = io.StringIO()');
      
      if (testInput !== null) {
        state.pyodide.runPython('_is_automated_test = True');
        const arr = testInput ? testInput.split('\\n') : [];
        state.pyodide.globals.set('_automated_inputs', state.pyodide.toPy(arr));
      } else {
        state.pyodide.runPython('_is_automated_test = False\\n_automated_inputs = []');
      }

      state.pyodide.runPython(code);
      const stdout = state.pyodide.runPython('sys.stdout.getvalue()');
      const stderr = state.pyodide.runPython('sys.stderr.getvalue()');
      return { output: stdout, error: stderr || '' };
    } catch (e) {
      let msg = e.message || String(e);
      const lines = msg.split('\\n').filter(l => l.trim());
      msg = lines.length > 0 ? lines[lines.length - 1] : msg;
      return { output: '', error: msg };
    }
  }

  // ===== CODEMIRROR =====
  function initEditor() {
    state.editor = CodeMirror($('code-editor-container'), {
      value: '',
      mode: 'python',
      theme: 'dracula',
      lineNumbers: true,
      indentUnit: 4,
      tabSize: 4,
      indentWithTabs: false,
      lineWrapping: true,
      matchBrackets: true,
      autoCloseBrackets: true,
      viewportMargin: Infinity,
      extraKeys: {
        'Ctrl-Enter': handleRun,
        'Cmd-Enter': handleRun,
        Tab: (cm) => cm.replaceSelection('    '),
      },
    });
  }

  // ===== CONTENT LOADING =====
  async function loadContent() {
    try {
      // Add timestamp to prevent caching during dev
      const resp = await fetch('default_content.json?t=' + Date.now());
      if (!resp.ok) throw new Error('Fetch failed');
      const data = await resp.json();
      state.categories = data.categories || [];
    } catch (e) {
      console.error('Failed to load content:', e);
      state.categories = [{
        id: "error_cat", title: "로딩 에러",
        lessons: [{
          id: "error_les", title: '로딩 실패',
          description: '## ⚠️ 콘텐츠를 불러올 수 없습니다.\\n\\n`default_content.json` 파일을 확인해 주세요.',
          initialCode: '# 로딩 실패', expectedOutput: '',
        }]
      }];
    }

    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE.PROGRESS) || '[]');
      state.completed = new Set(saved);
    } catch { state.completed = new Set(); }

    renderLessonList();
    loadLesson(0, 0);
    updateProgress();
  }

  // ===== RENDER LESSON LIST (Hierarchical) =====
  function renderLessonList() {
    const list = $('lesson-list');
    list.innerHTML = '';
    
    state.categories.forEach((category, cIndex) => {
      // 1. Category Header
      const catHeader = document.createElement('div');
      const isOpen = (cIndex === state.currentCatIndex);
      catHeader.className = 'category-header' + (isOpen ? ' open' : '');
      
      const catTitleWrap = document.createElement('div');
      catTitleWrap.style.cssText = "display:flex; align-items:center; flex:1; min-width:0; overflow:hidden;";
      catTitleWrap.innerHTML = `<span style="white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">📁 ${escapeHtml(category.title)}</span>`;
      catHeader.appendChild(catTitleWrap);

      if (state.mode === 'teacher') {
        const actions = document.createElement('div');
        actions.className = 'tc-inline-actions';
        
        const btnRename = document.createElement('button');
        btnRename.className = 'btn-icon';
        btnRename.textContent = '✏️';
        btnRename.title = '이름 변경';
        btnRename.addEventListener('click', (e) => { e.stopPropagation(); renameCategory(cIndex); });
        
        const btnDel = document.createElement('button');
        btnDel.className = 'btn-icon';
        btnDel.textContent = '🗑';
        btnDel.title = '단원 삭제';
        btnDel.addEventListener('click', (e) => { e.stopPropagation(); deleteCategory(cIndex); });

        actions.appendChild(btnRename);
        actions.appendChild(btnDel);
        catHeader.appendChild(actions);
      }

      const toggleWrap = document.createElement('span');
      toggleWrap.className = 'category-toggle';
      toggleWrap.style.marginLeft = '8px';
      toggleWrap.textContent = '▶';
      catHeader.appendChild(toggleWrap);
      
      // 2. Category Lessons Container
      const lessonsContainer = document.createElement('div');
      lessonsContainer.className = 'category-lessons' + (isOpen ? ' open' : '');
      
      catHeader.addEventListener('click', () => {
        catHeader.classList.toggle('open');
        lessonsContainer.classList.toggle('open');
      });
      list.appendChild(catHeader);

      // 3. Lessons
      (category.lessons || []).forEach((lesson, lIndex) => {
        const item = document.createElement('div');
        const isActive = (cIndex === state.currentCatIndex && lIndex === state.currentLesIndex);
        item.className = 'lesson-item' + (isActive ? ' active' : '');
        
        const done = state.completed.has(lesson.id);
        if (done) item.classList.add('completed');
        
        const lesTitleWrap = document.createElement('div');
        lesTitleWrap.style.cssText = "display:flex; align-items:center; flex:1; min-width:0; overflow:hidden;";
        lesTitleWrap.innerHTML = `
          <span class="lesson-status">${done ? '✅' : (isActive ? '▶' : '○')}</span>
          <span class="lesson-name" style="white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${escapeHtml(lesson.title)}</span>
        `;
        item.appendChild(lesTitleWrap);

        if (state.mode === 'teacher') {
          const actions = document.createElement('div');
          actions.className = 'tc-inline-actions';
          
          const btnRename = document.createElement('button');
          btnRename.className = 'btn-icon';
          btnRename.textContent = '✏️';
          btnRename.title = '이름 변경';
          btnRename.addEventListener('click', (e) => { e.stopPropagation(); renameLesson(cIndex, lIndex); });
          
          const btnDel = document.createElement('button');
          btnDel.className = 'btn-icon';
          btnDel.textContent = '🗑';
          btnDel.title = '단계 삭제';
          btnDel.addEventListener('click', (e) => { e.stopPropagation(); deleteLesson(cIndex, lIndex); });
          
          actions.appendChild(btnRename);
          actions.appendChild(btnDel);
          item.appendChild(actions);
        }

        item.addEventListener('click', () => {
          catHeader.classList.add('open');
          lessonsContainer.classList.add('open');
          loadLesson(cIndex, lIndex);
        });
        lessonsContainer.appendChild(item);
      });
      list.appendChild(lessonsContainer);
    });
  }

  // ===== GET CURRENT LESSON =====
  function getCurrentLesson() {
    return state.categories[state.currentCatIndex]?.lessons[state.currentLesIndex];
  }

  // ===== LOAD LESSON =====
  function loadLesson(cIndex, lIndex) {
    if (cIndex < 0 || cIndex >= state.categories.length) return;
    const category = state.categories[cIndex];
    if (lIndex < 0 || lIndex >= category.lessons.length) return;
    
    state.currentCatIndex = cIndex;
    state.currentLesIndex = lIndex;
    const lesson = category.lessons[lIndex];

    $('lesson-title').textContent = lesson.title;
    $('instruction-content').innerHTML = marked.parse(lesson.description || '');

    if (state.editor) {
      state.editor.setValue(lesson.initialCode || '');
      state.editor.clearHistory();
      setTimeout(() => state.editor.refresh(), 50);
    }

    $('output-terminal').innerHTML = '<span class="output-placeholder">코드를 실행하면 결과가 여기에 표시됩니다.</span>';
    $('validation-message').textContent = '';
    $('validation-message').className = '';

    $('btn-next').disabled = true;
    if (state.completed.has(lesson.id)) {
      $('btn-next').disabled = false;
    }

    if (state.mode === 'teacher') {
      $('edit-lesson-title').value = lesson.title;
      $('instruction-editor').value = lesson.description || '';
      renderTestCasesUI(lesson);
    }

    renderLessonList();
  }

  // ===== RUN CODE =====
  async function handleRun() {
    const code = state.editor.getValue();
    if (!code.trim()) {
      $('output-terminal').innerHTML = '<span class="output-placeholder">실행할 코드가 없습니다.</span>';
      return;
    }

    const terminal = $('output-terminal');
    terminal.innerHTML = '<span class="output-placeholder">⏳ 실행 중...</span>';
    $('btn-run').disabled = true;

    await new Promise(r => setTimeout(r, 50));
    const result = await runPython(code);
    $('btn-run').disabled = false;

    if (result.error) {
      terminal.innerHTML = `<span class="output-error">${escapeHtml(result.error)}</span>`;
      if (result.output) {
        terminal.innerHTML = `<span>${escapeHtml(result.output)}</span><span class="output-error">${escapeHtml(result.error)}</span>`;
      }
    } else {
      terminal.innerHTML = result.output ? escapeHtml(result.output) : '<span class="output-placeholder">(출력 없음)</span>';
    }

    if (state.mode === 'student') await validateOutput(code, result.output);
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // ===== VALIDATION =====
  async function validateOutput(code, interactiveOutput) {
    const lesson = getCurrentLesson();
    if (!lesson) return;

    const msgEl = $('validation-message');
    msgEl.textContent = '⏳ 채점 중...';
    msgEl.className = '';

    // Extract test cases (fallback to single expectedOutput for backward compatibility)
    let cases = lesson.testCases;
    if (!cases || cases.length === 0) {
      if (lesson.expectedOutput !== undefined && lesson.expectedOutput !== "") {
         cases = [{ input: "", expectedOutput: lesson.expectedOutput }];
      } else {
         msgEl.textContent = ''; // No validation required
         return;
      }
    }

    for (let i = 0; i < cases.length; i++) {
      const tc = cases[i];
      // Run background automated test
      const res = await runPython(code, tc.input || "");
      
      if (res.error) {
        msgEl.textContent = `❌ 테스트 케이스 ${i+1} 에러: ${res.error}`;
        msgEl.className = 'validation-fail';
        return; // Stop on first error
      }
      
      const actual = (res.output || '').trim();
      const expected = (tc.expectedOutput || '').trim();
      
      if (actual !== expected) {
        msgEl.textContent = `❌ 테스트 케이스 ${i+1} 실패 (입력: ${tc.input ? tc.input.replace(/\\n/g, ', ') : '없음'}, 예상: ${expected}, 실제: ${actual})`;
        msgEl.className = 'validation-fail';
        return; // Stop on first fail
      }
    }

    // All test cases passed!
    msgEl.textContent = '🎉 모든 테스트 케이스를 통과했습니다!';
    msgEl.className = 'validation-success';
    $('btn-next').disabled = false;

    state.completed.add(lesson.id);
    localStorage.setItem(STORAGE.PROGRESS, JSON.stringify([...state.completed]));
    updateProgress();
    renderLessonList();
  }

  // ===== PROGRESS =====
  function updateProgress() {
    let total = 0;
    state.categories.forEach(c => total += (c.lessons || []).length);
    const done = state.completed.size;
    const pct = total > 0 ? (done / total) * 100 : 0;
    $('progress-bar').style.width = pct + '%';
    $('progress-text').textContent = `${done} / ${total} 완료`;
  }

  // ===== MODE SWITCHING =====
  function toggleMode() {
    if (state.mode === 'student') {
      if (!state.authenticated) {
        show('login-modal');
        $('login-password').value = '';
        $('login-password').focus();
        hide('login-error');
        return;
      }
      enterTeacherMode();
    } else {
      exitTeacherMode();
    }
  }

  function enterTeacherMode() {
    state.mode = 'teacher';
    state.authenticated = true;
    const btn = $('mode-toggle');
    btn.classList.add('teacher');
    btn.querySelector('.mode-icon').textContent = '👨‍🏫';
    btn.querySelector('.mode-label').textContent = '선생님 모드';

    show('teacher-sidebar-actions');
    show('edit-lesson-title');
    show('teacher-desc-toolbar');
    show('instruction-editor-wrap');
    show('teacher-testcases-wrap');
    show('btn-save-lesson');
    hide('btn-next');

    const lesson = getCurrentLesson();
    if (lesson) {
      $('edit-lesson-title').value = lesson.title;
      $('instruction-editor').value = lesson.description || '';
      renderTestCasesUI(lesson);
    }

    hide('instruction-content');
    show('instruction-editor-wrap');
    state.isPreview = false;
    $('btn-preview-toggle').textContent = '👁 미리보기';
    toast('선생님 모드로 전환했습니다.', 'success');
  }

  function exitTeacherMode() {
    state.mode = 'student';
    const btn = $('mode-toggle');
    btn.classList.remove('teacher');
    btn.querySelector('.mode-icon').textContent = '👨‍🎓';
    btn.querySelector('.mode-label').textContent = '학생 모드';

    hide('teacher-sidebar-actions');
    hide('edit-lesson-title');
    hide('teacher-desc-toolbar');
    hide('instruction-editor-wrap');
    hide('teacher-testcases-wrap');
    hide('btn-save-lesson');
    hide('teacher-menu');
    show('btn-next');

    show('instruction-content');
    loadLesson(state.currentCatIndex, state.currentLesIndex);
    toast('학생 모드로 전환했습니다.');
  }

  // ===== TEACHER AUTH & CRUD =====
  async function handleLogin() {
    const pw = $('login-password').value;
    const hash = await sha256(pw);
    if (hash === getStoredHash()) {
      hide('login-modal');
      enterTeacherMode();
    } else {
      show('login-error');
    }
  }

  async function handleChangePassword() {
    const current = $('pw-current').value;
    const newPw = $('pw-new').value;
    const confirm = $('pw-confirm').value;
    const errEl = $('pw-error');

    const currentHash = await sha256(current);
    if (currentHash !== getStoredHash()) {
      errEl.textContent = '현재 비밀번호가 올바르지 않습니다.'; show(errEl); return;
    }
    if (newPw.length < 4) {
      errEl.textContent = '새 비밀번호는 4자 이상이어야 합니다.'; show(errEl); return;
    }
    if (newPw !== confirm) {
      errEl.textContent = '새 비밀번호가 일치하지 않습니다.'; show(errEl); return;
    }

    const newHash = await sha256(newPw);
    localStorage.setItem(STORAGE.PASSWORD, newHash);
    hide('password-modal');
    toast('비밀번호가 변경되었습니다.', 'success');
  }

  function renderTestCasesUI(lesson) {
    let cases = lesson.testCases;
    if (!cases || cases.length === 0) {
      if (lesson.expectedOutput !== undefined) {
         cases = [{ input: '', expectedOutput: lesson.expectedOutput }];
      } else {
         cases = [{ input: '', expectedOutput: '' }];
      }
    }
    // Deep copy to prevent mutating the original until saved
    state.editingTestCases = JSON.parse(JSON.stringify(cases));
    state.currentTcIndex = 0;
    renderCurrentTestCase();
  }

  function renderCurrentTestCase() {
    if (state.editingTestCases.length === 0) {
      state.editingTestCases.push({ input: '', expectedOutput: '' });
      state.currentTcIndex = 0;
    }
    
    const tc = state.editingTestCases[state.currentTcIndex];
    $('tc-input').value = tc.input || '';
    $('tc-expected').value = tc.expectedOutput || '';
    
    $('tc-indicator').textContent = `${state.currentTcIndex + 1} / ${state.editingTestCases.length}`;
    
    $('btn-tc-prev').disabled = (state.currentTcIndex === 0);
    $('btn-tc-next').disabled = (state.currentTcIndex === state.editingTestCases.length - 1);
  }

  function updateCurrentTestCaseData() {
    if (state.editingTestCases.length > 0) {
      state.editingTestCases[state.currentTcIndex].input = $('tc-input').value;
      state.editingTestCases[state.currentTcIndex].expectedOutput = $('tc-expected').value;
    }
  }

  function prevTestCase() {
    updateCurrentTestCaseData();
    if (state.currentTcIndex > 0) {
      state.currentTcIndex--;
      renderCurrentTestCase();
    }
  }

  function nextTestCase() {
    updateCurrentTestCaseData();
    if (state.currentTcIndex < state.editingTestCases.length - 1) {
      state.currentTcIndex++;
      renderCurrentTestCase();
    }
  }

  function addTestCase() {
    updateCurrentTestCaseData();
    state.editingTestCases.push({ input: '', expectedOutput: '' });
    state.currentTcIndex = state.editingTestCases.length - 1;
    renderCurrentTestCase();
  }

  function deleteTestCase() {
    if (state.editingTestCases.length <= 1) {
      toast('최소 1개의 테스트 케이스가 필요합니다.', 'error');
      return;
    }
    state.editingTestCases.splice(state.currentTcIndex, 1);
    if (state.currentTcIndex >= state.editingTestCases.length) {
      state.currentTcIndex = state.editingTestCases.length - 1;
    }
    renderCurrentTestCase();
  }

  function saveCurrentLesson() {
    const lesson = getCurrentLesson();
    if (!lesson) return;

    lesson.title = $('edit-lesson-title').value.trim() || '제목 없음';
    lesson.description = $('instruction-editor').value;
    lesson.initialCode = state.editor.getValue();
    
    // Save Test Cases
    updateCurrentTestCaseData();
    lesson.testCases = JSON.parse(JSON.stringify(state.editingTestCases));
    delete lesson.expectedOutput; // Cleanup old field

    $('lesson-title').textContent = lesson.title;
    renderLessonList();
    toast('💾 저장되었습니다.', 'success');
  }

  async function addLesson() {
    const cat = state.categories[state.currentCatIndex];
    if(!cat) return;
    
    const newTitle = await appPrompt('새 단계의 이름을 입력하세요:');
    if (!newTitle) return;
    
    const newId = 'l_' + Date.now();
    cat.lessons.push({
      id: newId,
      title: newTitle,
      description: '## 새 단계\\n\\n설명을 작성하세요.',
      initialCode: '# 코드를 작성하세요\\n',
      testCases: [{ input: '', expectedOutput: '' }]
    });
    renderLessonList();
    loadLesson(state.currentCatIndex, cat.lessons.length - 1);
    updateProgress();
    toast('새 단계가 추가되었습니다.', 'success');
  }

  async function deleteLesson(cIndex, lIndex) {
    const cat = state.categories[cIndex];
    if (cat.lessons.length <= 1) {
      toast('각 단원에는 최소 1개의 단계가 필요합니다.', 'error');
      return;
    }
    const lesson = cat.lessons[lIndex];
    if (!(await appConfirm(`정말로 "${lesson.title}" 단계를 삭제하시겠습니까?`))) return;

    cat.lessons.splice(lIndex, 1);
    
    if (state.currentCatIndex === cIndex) {
      if (state.currentLesIndex === lIndex) {
         state.currentLesIndex = Math.min(lIndex, cat.lessons.length - 1);
      } else if (state.currentLesIndex > lIndex) {
         state.currentLesIndex--;
      }
    }
    renderLessonList();
    if (state.currentCatIndex === cIndex) {
      loadLesson(state.currentCatIndex, state.currentLesIndex);
    }
    updateProgress();
    toast('삭제되었습니다.');
  }

  async function renameLesson(cIndex, lIndex) {
    const cat = state.categories[cIndex];
    const lesson = cat.lessons[lIndex];
    if (!lesson) return;
    
    const newTitle = await appPrompt('단계의 새 이름을 입력하세요:', lesson.title);
    if (!newTitle || newTitle.trim() === '' || newTitle === lesson.title) return;
    
    lesson.title = newTitle;
    if (state.currentCatIndex === cIndex && state.currentLesIndex === lIndex) {
      $('lesson-title').textContent = newTitle;
      if (state.mode === 'teacher') $('edit-lesson-title').value = newTitle;
    }
    renderLessonList();
    toast('단계 이름이 변경되었습니다.', 'success');
  }

  async function addCategory() {
    const newTitle = await appPrompt('새 단원의 이름을 입력하세요:');
    if (!newTitle) return;
    
    const newId = 'c_' + Date.now();
    state.categories.push({
      id: newId,
      title: newTitle,
      lessons: [{
        id: 'l_' + Date.now(),
        title: '새 학습 단계',
        description: '## 새 단계\\n\\n설명을 작성하세요.',
        initialCode: '# 코드를 작성하세요\\n',
        testCases: [{ input: '', expectedOutput: '' }]
      }]
    });
    
    renderLessonList();
    loadLesson(state.categories.length - 1, 0);
    updateProgress();
    toast('새 단원이 추가되었습니다.', 'success');
  }

  async function renameCategory(cIndex) {
    const cat = state.categories[cIndex];
    if (!cat) return;
    
    const newTitle = await appPrompt('단원의 새 이름을 입력하세요:', cat.title);
    if (!newTitle || newTitle.trim() === '' || newTitle === cat.title) return;
    
    cat.title = newTitle;
    renderLessonList();
    toast('단원 이름이 변경되었습니다.', 'success');
  }

  async function deleteCategory(cIndex) {
    if (state.categories.length <= 1) {
      toast('최소 1개의 단원이 필요합니다.', 'error');
      return;
    }
    const cat = state.categories[cIndex];
    if (!(await appConfirm(`정말로 "${cat.title}" 단원과 그 안의 모든 단계를 삭제하시겠습니까?`))) return;
    
    state.categories.splice(cIndex, 1);
    
    if (state.currentCatIndex === cIndex) {
      state.currentCatIndex = Math.min(cIndex, state.categories.length - 1);
      state.currentLesIndex = 0;
      loadLesson(state.currentCatIndex, state.currentLesIndex);
    } else if (state.currentCatIndex > cIndex) {
      state.currentCatIndex--;
    }
    renderLessonList();
    updateProgress();
    toast('단원이 삭제되었습니다.');
  }

  function downloadJSON() {
    if (state.mode === 'teacher') saveCurrentLesson();
    const data = JSON.stringify({ categories: state.categories }, null, 2);
    
    // 파일 프로토콜(file://) 등에서 Blob URL의 파일명이 무시되는 현상을 막기 위해 데이터 URI 방식 사용
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(data);
    const a = document.createElement('a');
    a.setAttribute('href', dataStr);
    a.setAttribute('download', 'default_content.json');
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    
    toast('📥 JSON 파일이 다운로드 되었습니다.', 'success');
  }

  function uploadJSON(file) {
    const reader = new FileReader();
    reader.onload = async (e) => {
      try {
        const data = JSON.parse(e.target.result);
        if (!data.categories || !Array.isArray(data.categories)) throw new Error('Invalid format');
        
        if (!(await appConfirm('기존 데이터를 모두 지우고 이 백업 파일의 내용으로 덮어씌우시겠습니까?'))) return;

        state.categories = data.categories;
        renderLessonList();
        loadLesson(0, 0);
        updateProgress();
        toast('📤 백업 콘텐츠를 성공적으로 복원했습니다.', 'success');
      } catch (err) {
        toast('❌ 올바른 JSON 파일이 아닙니다.', 'error');
      }
    };
    reader.readAsText(file);
  }

  function togglePreview() {
    state.isPreview = !state.isPreview;
    if (state.isPreview) {
      $('instruction-content').innerHTML = marked.parse($('instruction-editor').value);
      show('instruction-content'); hide('instruction-editor-wrap');
      $('btn-preview-toggle').textContent = '✏️ 편집';
    } else {
      hide('instruction-content'); show('instruction-editor-wrap');
      $('btn-preview-toggle').textContent = '👁 미리보기';
    }
  }

  // ===== RESIZER LOGIC =====
  function initResizer() {
    const resizer = $('resizer');
    const outputArea = $('output-area');
    const workPanel = $('work-panel');
    
    let isResizing = false;
    let startY = 0;
    let startHeight = 0;

    resizer.addEventListener('mousedown', (e) => {
      isResizing = true;
      startY = e.clientY;
      startHeight = outputArea.getBoundingClientRect().height;
      
      resizer.classList.add('active');
      document.body.style.cursor = 'row-resize';
      document.body.style.userSelect = 'none';
    });

    document.addEventListener('mousemove', (e) => {
      if (!isResizing) return;
      
      // Calculate how much the mouse moved UP
      const deltaY = startY - e.clientY;
      let newHeight = startHeight + deltaY;
      
      // Min and Max constraints
      const panelRect = workPanel.getBoundingClientRect();
      const minOutputHeight = 100;
      const maxOutputHeight = panelRect.height - 150; // Keep at least 150px for editor
      
      if (newHeight < minOutputHeight) newHeight = minOutputHeight;
      if (newHeight > maxOutputHeight) newHeight = maxOutputHeight;
      
      outputArea.style.flex = `0 0 ${newHeight}px`;
    });

    document.addEventListener('mouseup', () => {
      if (isResizing) {
        isResizing = false;
        resizer.classList.remove('active');
        document.body.style.cursor = 'default';
        document.body.style.userSelect = 'auto';
        if (state.editor) state.editor.refresh(); // Important for CodeMirror
      }
    });
  }

  function initHorizontalResizer() {
    const hResizer = $('h-resizer');
    const instructionPanel = $('instruction-panel');
    const appContainer = $('app-container');
    
    if (!hResizer) return;

    let isResizing = false;
    let startX = 0;
    let startWidth = 0;

    hResizer.addEventListener('mousedown', (e) => {
      isResizing = true;
      startX = e.clientX;
      startWidth = instructionPanel.getBoundingClientRect().width;
      
      hResizer.classList.add('active');
      document.body.style.cursor = 'col-resize';
      document.body.style.userSelect = 'none';
    });

    document.addEventListener('mousemove', (e) => {
      if (!isResizing) return;
      
      const deltaX = e.clientX - startX;
      let newWidth = startWidth + deltaX;
      
      const containerWidth = appContainer.getBoundingClientRect().width;
      const sidebarWidth = $('sidebar').getBoundingClientRect().width;
      const availableWidth = containerWidth - sidebarWidth;
      
      const minWidth = 250;
      const maxWidth = availableWidth - 300; // Keep at least 300px for work panel
      
      if (newWidth < minWidth) newWidth = minWidth;
      if (newWidth > maxWidth) newWidth = maxWidth;
      
      instructionPanel.style.flex = `0 0 ${newWidth}px`;
    });

    document.addEventListener('mouseup', () => {
      if (isResizing) {
        isResizing = false;
        hResizer.classList.remove('active');
        document.body.style.cursor = 'default';
        document.body.style.userSelect = 'auto';
        if (state.editor) state.editor.refresh();
      }
    });
  }

  // ===== EVENT BINDING =====
  function bindEvents() {
    $('btn-run').addEventListener('click', handleRun);
    $('btn-reset').addEventListener('click', () => {
      const lesson = getCurrentLesson();
      if (lesson) state.editor.setValue(lesson.initialCode || '');
    });
    $('btn-clear-output').addEventListener('click', () => {
      $('output-terminal').innerHTML = '<span class="output-placeholder">코드를 실행하면 결과가 여기에 표시됩니다.</span>';
      $('validation-message').textContent = '';
      $('validation-message').className = '';
    });

    // Next step (Cross-category navigation)
    $('btn-next').addEventListener('click', () => {
      const cat = state.categories[state.currentCatIndex];
      if (state.currentLesIndex < cat.lessons.length - 1) {
        // Next lesson in same category
        loadLesson(state.currentCatIndex, state.currentLesIndex + 1);
      } else if (state.currentCatIndex < state.categories.length - 1) {
        // Next category
        loadLesson(state.currentCatIndex + 1, 0);
        toast('다음 단원으로 넘어갑니다! 🚀', 'success');
      } else {
        toast('🎉 모든 단계를 완료했습니다! 대단해요!', 'success');
      }
    });

    $('mode-toggle').addEventListener('click', (e) => {
      if (state.mode === 'teacher') {
        state.teacherMenuOpen = !state.teacherMenuOpen;
        if (state.teacherMenuOpen) show('teacher-menu');
        else hide('teacher-menu');
      } else {
        toggleMode();
      }
    });

    $('sidebar-toggle').addEventListener('click', () => {
      const sb = $('sidebar');
      if (window.innerWidth <= 1024) sb.classList.toggle('open');
      else sb.classList.toggle('collapsed');
    });

    $('btn-login').addEventListener('click', handleLogin);
    $('login-password').addEventListener('keydown', (e) => { if (e.key === 'Enter') handleLogin(); });

    $('btn-change-password').addEventListener('click', () => {
      hide('teacher-menu'); state.teacherMenuOpen = false;
      show('password-modal');
      $('pw-current').value = ''; $('pw-new').value = ''; $('pw-confirm').value = '';
      hide('pw-error');
    });
    $('btn-change-pw').addEventListener('click', handleChangePassword);

    $('btn-logout').addEventListener('click', () => {
      hide('teacher-menu'); state.teacherMenuOpen = false;
      state.authenticated = false; exitTeacherMode();
    });

    document.querySelectorAll('.modal-close').forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.dataset.modal;
        if (target === 'prompt-modal') closePrompt(null);
        else if (target === 'confirm-modal') closeConfirm(false);
        else hide(target);
      });
    });

    document.querySelectorAll('.modal-overlay').forEach(overlay => {
      overlay.addEventListener('click', (e) => { 
        if (e.target === overlay) {
          if (overlay.id === 'prompt-modal') closePrompt(null);
          else if (overlay.id === 'confirm-modal') closeConfirm(false);
          else hide(overlay);
        } 
      });
    });

    $('btn-prompt-confirm').addEventListener('click', () => closePrompt($('prompt-input').value));
    $('prompt-input').addEventListener('keydown', (e) => { if (e.key === 'Enter') closePrompt($('prompt-input').value); });
    $('btn-confirm-yes').addEventListener('click', () => closeConfirm(true));

    document.addEventListener('click', (e) => {
      if (state.teacherMenuOpen && !$('mode-toggle').contains(e.target) && !$('teacher-menu').contains(e.target)) {
        hide('teacher-menu'); state.teacherMenuOpen = false;
      }
    });

    $('btn-save-lesson').addEventListener('click', saveCurrentLesson);
    $('btn-add-lesson').addEventListener('click', addLesson);
    $('btn-add-category').addEventListener('click', addCategory);
    $('btn-download-json').addEventListener('click', downloadJSON);
    $('btn-upload-json').addEventListener('click', () => $('json-file-input').click());
    $('json-file-input').addEventListener('change', (e) => {
      if (e.target.files[0]) uploadJSON(e.target.files[0]);
      e.target.value = '';
    });

    $('btn-preview-toggle').addEventListener('click', togglePreview);
    
    $('btn-tc-prev').addEventListener('click', prevTestCase);
    $('btn-tc-next').addEventListener('click', nextTestCase);
    $('btn-add-testcase').addEventListener('click', addTestCase);
    $('btn-tc-delete').addEventListener('click', deleteTestCase);
    
    $('tc-input').addEventListener('input', updateCurrentTestCaseData);
    $('tc-expected').addEventListener('input', updateCurrentTestCaseData);

    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault(); handleRun();
      }
    });

    initResizer();
    initHorizontalResizer();
  }

  // ===== INIT =====
  async function init() {
    $('btn-run').disabled = true;
    initEditor();
    bindEvents();
    await loadContent();
    initPyodide();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

})();
