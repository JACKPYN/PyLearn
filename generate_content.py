import json

data = {
    "categories": [
        {
            "id": "c1",
            "title": "1단원: 입출력 (Input/Output)",
            "lessons": [
                {
                    "id": "c1_l1", "title": "1. 첫 번째 파이썬 프로그램",
                    "description": "## 🎉 파이썬의 세계에 오신 것을 환영합니다!\n\n파이썬에서 화면에 글자를 보여주려면 `print()` 함수를 사용합니다.\n\n### 사용법\n```python\nprint(\"안녕, 파이썬!\")\n```\n\n> 💡 **팁**: 문자열은 큰따옴표(`\"`) 또는 작은따옴표(`'`)로 감싸야 합니다.\n\n---\n\n### ✏️ 미션\n화면에 `Hello, World!`를 출력해보세요.",
                    "initialCode": "# 아래에 코드를 작성하세요\n", "expectedOutput": "Hello, World!"
                },
                {
                    "id": "c1_l2", "title": "2. 여러 줄 출력하기",
                    "description": "## 📝 여러 번 출력하기\n\n`print()` 함수를 여러 번 쓰면 여러 줄에 걸쳐 출력할 수 있습니다.\n\n```python\nprint(\"첫 번째 줄\")\nprint(\"두 번째 줄\")\n```\n\n---\n\n### ✏️ 미션\n`Python`과 `is fun!`을 각각 다른 줄에 출력해보세요.",
                    "initialCode": "# 두 번의 print()를 사용하세요\n", "expectedOutput": "Python\nis fun!"
                },
                {
                    "id": "c1_l3", "title": "3. 숫자 출력하기",
                    "description": "## 🔢 숫자 출력\n\n숫자는 따옴표 없이 그대로 `print()`에 넣을 수 있습니다.\n\n```python\nprint(100)\nprint(3.14)\n```\n\n---\n\n### ✏️ 미션\n자신의 나이를(예: `20`) 숫자로 출력해보세요. (정답 검증을 위해 `20`을 출력하세요)",
                    "initialCode": "# 숫자를 출력하세요\n", "expectedOutput": "20"
                },
                {
                    "id": "c1_l4", "title": "4. 문자열 연결하기",
                    "description": "## 🔗 글자 이어 붙이기\n\n문자열끼리 `+` 기호를 사용하면 하나의 문자열로 이어붙일 수 있습니다.\n\n```python\nprint(\"안녕\" + \"하세요\") # 안녕하세요\n```\n\n---\n\n### ✏️ 미션\n`\"Hello\"`와 `\"World\"`를 `+`로 이어붙여서 `HelloWorld`를 출력하세요. (공백 없이)",
                    "initialCode": "# 문자열을 이어 붙이세요\n", "expectedOutput": "HelloWorld"
                },
                {
                    "id": "c1_l5", "title": "5. 여러 값 함께 출력하기",
                    "description": "## 콤마(,)로 여러 개 출력\n\n`print()` 안에 여러 값을 콤마(`,`)로 구분해서 넣으면 공백(띄어쓰기)으로 구분되어 출력됩니다.\n\n```python\nprint(\"이름:\", \"홍길동\") # 이름: 홍길동\n```\n\n---\n\n### ✏️ 미션\n콤마를 사용하여 `Name:`과 `Python`을 함께 출력하세요.",
                    "initialCode": "# 콤마로 구분하여 출력하세요\n", "expectedOutput": "Name: Python"
                },
                {
                    "id": "c1_l6", "title": "6. 따옴표 출력하기",
                    "description": "## \" \" 안에 ' ' 쓰기\n\n출력할 텍스트 안에 따옴표를 넣고 싶다면, 다른 종류의 따옴표로 전체를 감싸면 됩니다.\n\n```python\nprint(\"그는 '안녕'이라고 말했다.\")\n```\n\n---\n\n### ✏️ 미션\n`I'm a programmer`를 출력하세요.",
                    "initialCode": "# 큰따옴표 안에 작은따옴표를 사용해 보세요\n", "expectedOutput": "I'm a programmer"
                },
                {
                    "id": "c1_l7", "title": "7. 이스케이프 문자 (줄바꿈)",
                    "description": "## `\\n` 으로 줄 바꾸기\n\n문자열 중간에 `\\n`을 넣으면 그 위치에서 줄이 바뀝니다.\n\n```python\nprint(\"안녕\\n하세요\")\n```\n\n---\n\n### ✏️ 미션\n`\\n`을 사용하여 한 번의 `print()`로 다음과 같이 두 줄로 출력하세요.\n```text\nOne\nTwo\n```",
                    "initialCode": "# \\n을 사용하세요\n", "expectedOutput": "One\nTwo"
                },
                {
                    "id": "c1_l8", "title": "8. sep 옵션 사용하기",
                    "description": "## 🔄 구분자 바꾸기 (`sep`)\n\n여러 값을 출력할 때 콤마를 쓰면 기본적으로 공백이 들어갑니다. `sep` 옵션을 쓰면 이 공백을 다른 문자로 바꿀 수 있습니다.\n\n```python\nprint(\"A\", \"B\", \"C\", sep=\"-\") # A-B-C\n```\n\n---\n\n### ✏️ 미션\n`2026`, `04`, `18`을 콤마로 넣고, `sep=\"-\"`를 사용하여 `2026-04-18`로 출력하세요.",
                    "initialCode": "# sep 옵션을 사용하세요\nprint(2026, \"04\", 18)\n", "expectedOutput": "2026-04-18"
                },
                {
                    "id": "c1_l9", "title": "9. end 옵션 사용하기",
                    "description": "## 🛑 끝 문자 바꾸기 (`end`)\n\n`print()`는 기본적으로 출력이 끝나면 줄바꿈을 합니다. `end` 옵션을 쓰면 줄바꿈 대신 다른 문자를 넣을 수 있습니다.\n\n```python\nprint(\"Hello\", end=\" \")\nprint(\"World\")\n# Hello World (한 줄에 출력됨)\n```\n\n---\n\n### ✏️ 미션\n`end=\"\"`(빈 문자열)을 사용하여 두 번의 print()가 한 줄에 `ABC`로 출력되게 하세요.",
                    "initialCode": "print(\"A\")\nprint(\"BC\")\n", "expectedOutput": "ABC"
                },
                {
                    "id": "c1_l10", "title": "10. 데이터 입력받기 (input)",
                    "description": "## ⌨️ 사용자 입력 (`input()`)\n\n사용자에게 값을 입력받을 때는 `input()`을 사용합니다.\n\n```python\nname = input(\"이름을 입력하세요: \")\nprint(name)\n```\n*(PyLearn 환경에서는 `input()` 실행 시 브라우저 팝업이 뜹니다.)*\n\n---\n\n### ✏️ 미션\n`input()`으로 문자열을 입력받아 변수 `word`에 저장한 뒤, 그대로 출력하세요. (팝업창에 `PyLearn`이라고 입력해보세요.)",
                    "initialCode": "# 입력을 받아 출력하세요\n", "expectedOutput": "PyLearn"
                }
            ]
        },
        {
            "id": "c2",
            "title": "2단원: 변수와 연산자",
            "lessons": [
                {
                    "id": "c2_l1", "title": "1. 변수 만들기",
                    "description": "## 📦 값을 담는 상자, 변수\n\n변수는 값을 저장하는 공간입니다. `=` 기호를 사용하여 이름을 지어주고 값을 넣습니다.\n\n```python\nx = 10\nprint(x)\n```\n\n---\n\n### ✏️ 미션\n`my_number`라는 변수를 만들고 값 `50`을 넣은 뒤, `print()`로 출력하세요.",
                    "initialCode": "# 변수를 만들고 출력하세요\n", "expectedOutput": "50"
                },
                {
                    "id": "c2_l2", "title": "2. 변수 값 변경하기",
                    "description": "## 🔄 변수 값 바꾸기\n\n이미 만들어진 변수에 새로운 값을 넣으면 이전 값은 지워지고 새 값이 저장됩니다.\n\n```python\na = 5\na = 10  # 5 대신 10으로 바뀜\n```\n\n---\n\n### ✏️ 미션\n변수 `score`의 값을 `100`으로 바꾼 뒤 출력하세요.",
                    "initialCode": "score = 0\n# 여기서 score 값을 100으로 변경하세요\n\nprint(score)\n", "expectedOutput": "100"
                },
                {
                    "id": "c2_l3", "title": "3. 덧셈과 뺄셈",
                    "description": "## ➕ ➖ 사칙연산\n\n파이썬은 훌륭한 계산기입니다.\n\n```python\nprint(10 + 5)\nprint(20 - 8)\n```\n\n---\n\n### ✏️ 미션\n변수 `a`에 15, `b`에 7을 넣고 두 값의 합을 출력하세요.",
                    "initialCode": "a = 15\nb = 7\n# 두 수의 합을 출력하세요\n", "expectedOutput": "22"
                },
                {
                    "id": "c2_l4", "title": "4. 곱셈과 나눗셈",
                    "description": "## ✖️ ➗ 곱하기와 나누기\n\n곱셈은 `*`, 나눗셈은 `/` 기호를 사용합니다.\n\n```python\nprint(4 * 3)  # 12\nprint(10 / 2) # 5.0 (나눗셈의 결과는 항상 실수형입니다)\n```\n\n---\n\n### ✏️ 미션\n`6 * 8`의 결과를 출력하세요.",
                    "initialCode": "# 6과 8의 곱을 출력하세요\n", "expectedOutput": "48"
                },
                {
                    "id": "c2_l5", "title": "5. 몫과 나머지",
                    "description": "## 🍕 몫(`//`)과 나머지(`%`)\n\n나눗셈의 몫만 구하려면 `//`, 나머지만 구하려면 `%`를 씁니다.\n짝수/홀수 판별 등에 아주 많이 쓰입니다.\n\n```python\nprint(10 // 3) # 3\nprint(10 % 3)  # 1\n```\n\n---\n\n### ✏️ 미션\n`17`을 `5`로 나눈 **나머지**를 출력하세요.",
                    "initialCode": "# 17을 5로 나눈 나머지를 계산하여 출력하세요\n", "expectedOutput": "2"
                },
                {
                    "id": "c2_l6", "title": "6. 거듭제곱",
                    "description": "## 🚀 거듭제곱 (`**`)\n\n어떤 수를 여러 번 곱하는 거듭제곱은 `**` 기호를 사용합니다.\n\n```python\nprint(2 ** 3) # 2의 3제곱 = 8\n```\n\n---\n\n### ✏️ 미션\n`3`의 `4`제곱을 계산하여 출력하세요.",
                    "initialCode": "# 3의 4제곱을 출력하세요\n", "expectedOutput": "81"
                },
                {
                    "id": "c2_l7", "title": "7. 문자열 곱하기",
                    "description": "## 🔁 문자열 반복\n\n파이썬만의 독특한 기능! 문자열에 숫자를 곱하면 그 수만큼 반복됩니다.\n\n```python\nprint(\"안녕\" * 3) # 안녕안녕안녕\n```\n\n---\n\n### ✏️ 미션\n`\"Ha\"`라는 문자열에 `5`를 곱해서 출력하세요.",
                    "initialCode": "# 문자열 반복을 사용하세요\n", "expectedOutput": "HaHaHaHaHa"
                },
                {
                    "id": "c2_l8", "title": "8. 데이터 타입 (type)",
                    "description": "## 🏷️ 자료형 확인하기 (`type()`)\n\n변수 안에 들어있는 값이 숫자인지 문자인지 알고 싶다면 `type()` 함수를 사용합니다.\n\n```python\nprint(type(10))    # <class 'int'> (정수)\nprint(type(\"안녕\")) # <class 'str'> (문자열)\n```\n\n---\n\n### ✏️ 미션\n실수형 값인 `3.14`의 데이터 타입을 출력하세요. (기대 출력: `<class 'float'>`)",
                    "initialCode": "# 3.14의 타입을 출력하세요\n", "expectedOutput": "<class 'float'>"
                },
                {
                    "id": "c2_l9", "title": "9. 타입 변환 (형변환)",
                    "description": "## 🔄 자료형 바꾸기\n\n문자열로 된 숫자는 계산할 수 없습니다. `int()`를 사용해 정수로 바꿔주어야 합니다.\n\n```python\ntext_num = \"10\"\nreal_num = int(text_num)\nprint(real_num + 5) # 15\n```\n\n---\n\n### ✏️ 미션\n문자열 `\"20\"`을 정수로 변환하여 숫자 `30`과 더한 결과를 출력하세요.",
                    "initialCode": "a = \"20\"\nb = 30\n# a를 정수로 바꾼 뒤 b와 더해서 출력하세요\n", "expectedOutput": "50"
                },
                {
                    "id": "c2_l10", "title": "10. 복합 대입 연산자",
                    "description": "## ⚡ 더 빨리 계산하기\n\n변수에 연산 후 자기 자신에게 다시 값을 넣을 때 줄여서 쓸 수 있습니다.\n\n```python\nx = 10\nx = x + 5  # 기존 방식\nx += 5     # 똑같은 의미! (결과는 15)\n```\n\n---\n\n### ✏️ 미션\n변수 `count`에 `+= 10`을 사용하여 값을 증가시킨 후 출력하세요.",
                    "initialCode": "count = 5\n# count를 10 증가시키세요\n\nprint(count)\n", "expectedOutput": "15"
                }
            ]
        },
        {
            "id": "c3",
            "title": "3단원: 리스트 (List)",
            "lessons": [
                {
                    "id": "c3_l1", "title": "1. 리스트 만들기",
                    "description": "## 📋 여러 값을 한 번에!\n\n리스트는 여러 개의 데이터를 한 곳에 모아두는 바구니입니다. 대괄호 `[]`를 사용합니다.\n\n```python\nfruits = [\"사과\", \"바나나\", \"오렌지\"]\nprint(fruits)\n```\n\n---\n\n### ✏️ 미션\n`1`, `2`, `3` 세 개의 숫자가 들어있는 리스트 `numbers`를 만들고 출력하세요.",
                    "initialCode": "# 리스트를 만들고 출력하세요\n", "expectedOutput": "[1, 2, 3]"
                },
                {
                    "id": "c3_l2", "title": "2. 리스트 요소 꺼내기 (인덱싱)",
                    "description": "## 🎯 인덱싱 (Indexing)\n\n리스트에서 특정 위치의 값을 꺼낼 수 있습니다. 주의할 점: **파이썬은 0부터 숫자를 셉니다!**\n\n```python\ncolors = [\"빨강\", \"파랑\", \"노랑\"]\nprint(colors[0]) # 첫 번째 값인 '빨강'\n```\n\n---\n\n### ✏️ 미션\n`animals` 리스트에서 두 번째 값(`\"cat\"`)을 출력하세요.",
                    "initialCode": "animals = [\"dog\", \"cat\", \"bird\"]\n# cat을 출력하세요\n", "expectedOutput": "cat"
                },
                {
                    "id": "c3_l3", "title": "3. 음수 인덱스",
                    "description": "## 🔙 뒤에서부터 세기\n\n리스트의 마지막 값을 꺼낼 때는 `-1`을 쓰면 편리합니다.\n\n```python\ncolors = [\"빨강\", \"파랑\", \"노랑\"]\nprint(colors[-1]) # 마지막 값인 '노랑'\n```\n\n---\n\n### ✏️ 미션\n주어진 리스트에서 음수 인덱스를 사용하여 마지막 값 `\"C\"`를 출력하세요.",
                    "initialCode": "chars = [\"A\", \"B\", \"C\"]\n# 마지막 값을 출력하세요\n", "expectedOutput": "C"
                },
                {
                    "id": "c3_l4", "title": "4. 리스트 부분 자르기 (슬라이싱)",
                    "description": "## ✂️ 슬라이싱 (Slicing)\n\n`리스트[시작위치:끝위치]`를 사용하면 리스트의 일부분만 잘라낼 수 있습니다.\n*끝 위치의 값은 포함되지 않습니다!*\n\n```python\nnums = [0, 1, 2, 3, 4]\nprint(nums[1:3]) # 1번 인덱스부터 2번 인덱스까지 -> [1, 2]\n```\n\n---\n\n### ✏️ 미션\n리스트에서 두 번째와 세 번째 항목만 잘라내어 `[20, 30]`을 출력하세요.",
                    "initialCode": "data = [10, 20, 30, 40, 50]\n# [20, 30]이 출력되게 하세요\n", "expectedOutput": "[20, 30]"
                },
                {
                    "id": "c3_l5", "title": "5. 리스트 항목 추가 (append)",
                    "description": "## ➕ 리스트 끝에 추가하기\n\n`.append()` 함수를 사용하면 리스트의 맨 마지막에 새로운 항목을 추가할 수 있습니다.\n\n```python\nitems = [\"사과\"]\nitems.append(\"바나나\")\nprint(items) # ['사과', '바나나']\n```\n\n---\n\n### ✏️ 미션\n`scores` 리스트에 `100`을 추가한 뒤 리스트를 출력하세요.",
                    "initialCode": "scores = [80, 90]\n# 100을 추가하세요\n\nprint(scores)\n", "expectedOutput": "[80, 90, 100]"
                },
                {
                    "id": "c3_l6", "title": "6. 원하는 위치에 추가 (insert)",
                    "description": "## 📌 중간에 끼워넣기\n\n`.insert(위치, 값)`을 사용하면 원하는 인덱스에 값을 끼워넣을 수 있습니다.\n\n```python\nitems = [\"A\", \"C\"]\nitems.insert(1, \"B\") # 1번 위치에 \"B\" 추가\nprint(items) # ['A', 'B', 'C']\n```\n\n---\n\n### ✏️ 미션\n`names` 리스트의 맨 앞(0번 위치)에 `\"Zero\"`를 추가하고 출력하세요.",
                    "initialCode": "names = [\"One\", \"Two\"]\n# 0번 위치에 \"Zero\"를 추가하세요\n\nprint(names)\n", "expectedOutput": "['Zero', 'One', 'Two']"
                },
                {
                    "id": "c3_l7", "title": "7. 리스트 항목 삭제 (remove)",
                    "description": "## 🗑️ 값으로 삭제하기\n\n`.remove(값)`을 사용하면 리스트에서 해당 값을 찾아 삭제합니다.\n\n```python\nitems = [\"A\", \"B\", \"C\"]\nitems.remove(\"B\")\nprint(items) # ['A', 'C']\n```\n\n---\n\n### ✏️ 미션\n`fruits` 리스트에서 `\"Apple\"`을 지운 후 출력하세요.",
                    "initialCode": "fruits = [\"Apple\", \"Banana\", \"Cherry\"]\n# \"Apple\"을 삭제하세요\n\nprint(fruits)\n", "expectedOutput": "['Banana', 'Cherry']"
                },
                {
                    "id": "c3_l8", "title": "8. 리스트 마지막 항목 꺼내기 (pop)",
                    "description": "## 📤 마지막 값 뽑아내기\n\n`.pop()`은 리스트의 맨 마지막 요소를 리스트에서 삭제함과 동시에 그 값을 반환합니다.\n\n```python\nitems = [1, 2, 3]\nlast = items.pop()\nprint(items) # [1, 2]\nprint(last)  # 3\n```\n\n---\n\n### ✏️ 미션\n`data` 리스트에서 `pop()`을 호출하고, 빠져나온 그 값(`30`)을 출력하세요.",
                    "initialCode": "data = [10, 20, 30]\n# pop()을 사용하여 마지막 값을 출력하세요\n", "expectedOutput": "30"
                },
                {
                    "id": "c3_l9", "title": "9. 리스트 길이 구하기 (len)",
                    "description": "## 📏 개수 확인하기\n\n`len()` 함수를 사용하면 리스트 안에 몇 개의 항목이 들어있는지 알 수 있습니다.\n\n```python\nitems = [\"가\", \"나\", \"다\"]\nprint(len(items)) # 3\n```\n\n---\n\n### ✏️ 미션\n`words` 리스트의 항목 개수를 구하여 출력하세요.",
                    "initialCode": "words = [\"Python\", \"is\", \"fun\", \"!\"]\n# words의 길이를 출력하세요\n", "expectedOutput": "4"
                },
                {
                    "id": "c3_l10", "title": "10. 리스트 정렬하기 (sort)",
                    "description": "## 🔠 정렬하기\n\n`.sort()` 함수를 사용하면 리스트의 내용을 오름차순(작은 순서대로)으로 정렬해줍니다.\n\n```python\nnums = [3, 1, 2]\nnums.sort()\nprint(nums) # [1, 2, 3]\n```\n\n---\n\n### ✏️ 미션\n`numbers` 리스트를 정렬한 후 출력하세요.",
                    "initialCode": "numbers = [5, 2, 8, 1, 9]\n# 정렬하고 출력하세요\n", "expectedOutput": "[1, 2, 5, 8, 9]"
                }
            ]
        },
        {
            "id": "c4",
            "title": "4단원: 조건문 (If / Else)",
            "lessons": [
                {
                    "id": "c4_l1", "title": "1. 참과 거짓 (Boolean)",
                    "description": "## ⚖️ True 와 False\n\n파이썬에는 참(`True`)과 거짓(`False`)을 나타내는 자료형이 있습니다. 첫 글자는 무조건 대문자여야 합니다!\n\n```python\nis_raining = True\nprint(is_raining)\n```\n\n---\n\n### ✏️ 미션\n변수 `is_fun`에 `True` 값을 넣고 출력하세요.",
                    "initialCode": "# is_fun 변수를 만들고 출력하세요\n", "expectedOutput": "True"
                },
                {
                    "id": "c4_l2", "title": "2. 비교 연산자",
                    "description": "## ⚖️ 크기 비교하기\n\n비교 연산의 결과는 항상 `True` 또는 `False`입니다.\n- `==` (같다), `!=` (다르다)\n- `>` (크다), `<` (작다), `>=`, `<=`\n\n```python\nprint(10 > 5)  # True\nprint(3 == 4)  # False\n```\n\n---\n\n### ✏️ 미션\n`10`과 `10`이 서로 같은지 비교하는 수식을 `print()`로 출력하세요. (기대 출력: `True`)",
                    "initialCode": "# 10과 10이 같은지 비교하세요\n", "expectedOutput": "True"
                },
                {
                    "id": "c4_l3", "title": "3. if 문 기본",
                    "description": "## 🔀 만약 ~라면\n\n`if` 문은 조건이 참일 때만 코드를 실행합니다. 들여쓰기(띄어쓰기 4칸)가 매우 중요합니다!\n\n```python\nif 10 > 5:\n    print(\"10이 더 큽니다.\")\n```\n\n---\n\n### ✏️ 미션\n`score`가 80보다 크면 `\"합격\"`을 출력하도록 if 문을 완성하세요.",
                    "initialCode": "score = 90\n# if 문을 작성하세요\n", "expectedOutput": "합격"
                },
                {
                    "id": "c4_l4", "title": "4. else 문",
                    "description": "## 🔀 그렇지 않다면 (else)\n\n조건이 참이 아닐 때 실행할 코드는 `else`에 적습니다.\n\n```python\nage = 15\nif age >= 20:\n    print(\"성인\")\nelse:\n    print(\"미성년자\")\n```\n\n---\n\n### ✏️ 미션\n변수 `x`가 `10`보다 작으면 `\"작음\"`, 아니면 `\"큼\"`을 출력하도록 작성하세요. 현재 x는 15입니다.",
                    "initialCode": "x = 15\n# if-else 구문을 작성하세요\n", "expectedOutput": "큼"
                },
                {
                    "id": "c4_l5", "title": "5. elif 문",
                    "description": "## 🔀 여러 조건 처리하기 (elif)\n\n`else if`의 줄임말인 `elif`를 사용하면 여러 조건을 연달아 검사할 수 있습니다.\n\n```python\ncolor = \"red\"\nif color == \"blue\":\n    print(\"파랑\")\nelif color == \"red\":\n    print(\"빨강\")\nelse:\n    print(\"기타\")\n```\n\n---\n\n### ✏️ 미션\n`score`가 90 이상이면 `\"A\"`, 80 이상이면 `\"B\"`, 그 외는 `\"C\"`를 출력하세요.",
                    "initialCode": "score = 85\n# 코드를 완성하세요\n", "expectedOutput": "B"
                },
                {
                    "id": "c4_l6", "title": "6. 논리 연산자 (and)",
                    "description": "## 🤝 둘 다 참이어야 참! (and)\n\n두 조건이 모두 만족해야 할 때는 `and`를 사용합니다.\n\n```python\nprint(True and True)   # True\nprint(True and False)  # False\n```\n\n---\n\n### ✏️ 미션\n`age`가 10 이상 **그리고** 20 미만이면 `\"10대입니다\"`를 출력하세요.",
                    "initialCode": "age = 15\n# and 연산자를 사용하여 if 문을 작성하세요\n", "expectedOutput": "10대입니다"
                },
                {
                    "id": "c4_l7", "title": "7. 논리 연산자 (or)",
                    "description": "## 👐 하나라도 참이면 참! (or)\n\n두 조건 중 하나라도 만족하면 될 때는 `or`를 사용합니다.\n\n```python\nprint(True or False)  # True\nprint(False or False) # False\n```\n\n---\n\n### ✏️ 미션\n`money`가 5000 이상이거나 `card`가 `True`이면 `\"택시 타기\"`를 출력하세요.",
                    "initialCode": "money = 3000\ncard = True\n# or 연산자를 사용하세요\n", "expectedOutput": "택시 타기"
                },
                {
                    "id": "c4_l8", "title": "8. 논리 연산자 (not)",
                    "description": "## 🚫 반대로 만들기 (not)\n\n`not`은 참/거짓 값을 반대로 뒤집어줍니다.\n\n```python\nprint(not True)  # False\n```\n\n---\n\n### ✏️ 미션\n변수 `is_tired`가 `False`입니다. `not`을 사용해서 이것을 뒤집어 `True`를 출력해보세요.",
                    "initialCode": "is_tired = False\n# not을 사용하여 True가 출력되게 하세요\n", "expectedOutput": "True"
                },
                {
                    "id": "c4_l9", "title": "9. 리스트와 조건문 (in)",
                    "description": "## 🔍 리스트 안에 값이 있는지 확인 (in)\n\n`in` 키워드를 쓰면 특정 값이 리스트 안에 포함되어 있는지 쉽게 확인할 수 있습니다.\n\n```python\nfruits = [\"사과\", \"포도\"]\nif \"사과\" in fruits:\n    print(\"사과가 있습니다.\")\n```\n\n---\n\n### ✏️ 미션\n`\"Banana\"`가 `basket` 리스트에 있다면 `\"바나나 있음\"`을 출력하세요.",
                    "initialCode": "basket = [\"Apple\", \"Banana\", \"Orange\"]\n# in 키워드를 사용하세요\n", "expectedOutput": "바나나 있음"
                },
                {
                    "id": "c4_l10", "title": "10. 중첩 조건문",
                    "description": "## 🪆 if 안에 if 넣기\n\n`if` 구문 안에 또 다른 `if` 구문을 넣어 더 상세한 조건을 체크할 수 있습니다. 이때 들여쓰기가 두 번(8칸) 들어갑니다.\n\n```python\nif age > 18:\n    if has_license:\n        print(\"운전 가능\")\n```\n\n---\n\n### ✏️ 미션\n`is_member`가 `True`일 때, 다시 `point`가 100 이상이면 `\"VIP\"`를 출력하는 중첩 코드를 완성하세요.",
                    "initialCode": "is_member = True\npoint = 150\n\n# if 안에 if를 작성하세요\n", "expectedOutput": "VIP"
                }
            ]
        },
        {
            "id": "c5",
            "title": "5단원: 반복문 (Loop)",
            "lessons": [
                {
                    "id": "c5_l1", "title": "1. for 반복문과 리스트",
                    "description": "## 🔁 리스트 순회하기\n\n`for 변수 in 리스트:` 형식을 쓰면 리스트의 요소들을 처음부터 끝까지 하나씩 꺼내며 반복합니다.\n\n```python\ncolors = [\"빨\", \"주\", \"노\"]\nfor c in colors:\n    print(c)\n```\n\n---\n\n### ✏️ 미션\n`numbers` 리스트의 숫자들을 `for` 문을 사용하여 하나씩 줄바꿈하여 출력하세요.",
                    "initialCode": "numbers = [1, 2, 3]\n# for 문을 작성하세요\n", "expectedOutput": "1\n2\n3"
                },
                {
                    "id": "c5_l2", "title": "2. range() 함수 기본",
                    "description": "## 🔢 숫자 생성기 range()\n\n특정 횟수만큼 반복하고 싶을 때는 `range(횟수)`를 사용합니다. 0부터 시작합니다.\n\n```python\nfor i in range(3):\n    print(\"안녕\") # 안녕 이 3번 출력됨\n```\n\n---\n\n### ✏️ 미션\n`range()`를 사용하여 `0`부터 `4`까지 한 줄씩 출력하세요.",
                    "initialCode": "# for 와 range(5)를 사용하세요\n", "expectedOutput": "0\n1\n2\n3\n4"
                },
                {
                    "id": "c5_l3", "title": "3. range() 시작과 끝",
                    "description": "## 🎯 구간 지정하기\n\n`range(시작, 끝)` 처럼 2개의 숫자를 넣으면 '시작 값부터 끝 값 바로 전까지' 반복합니다.\n\n```python\nfor i in range(1, 4):\n    print(i) # 1, 2, 3 출력\n```\n\n---\n\n### ✏️ 미션\n`range(5, 8)`을 사용하여 `5`, `6`, `7`을 한 줄씩 출력하세요.",
                    "initialCode": "# 시작과 끝을 지정한 range()를 사용하세요\n", "expectedOutput": "5\n6\n7"
                },
                {
                    "id": "c5_l4", "title": "4. while 반복문",
                    "description": "## ⏳ 조건이 참인 동안 (while)\n\n`while 조건:` 형식을 쓰면 조건이 `True`인 동안 코드를 무한히 반복합니다. 반드시 종료 조건을 만들어주어야 합니다!\n\n```python\nx = 1\nwhile x <= 3:\n    print(x)\n    x = x + 1\n```\n\n---\n\n### ✏️ 미션\n`while` 문을 사용하여 `count`가 3보다 작거나 같을 때까지 `count` 값을 출력하세요.",
                    "initialCode": "count = 1\n# while 문을 완성하세요 (count 1씩 증가시키는 것 잊지 마세요!)\n", "expectedOutput": "1\n2\n3"
                },
                {
                    "id": "c5_l5", "title": "5. 반복문 탈출 (break)",
                    "description": "## 🚪 즉시 멈춰! (break)\n\n반복문 안에서 `break`를 만나면 반복문이 조건과 상관없이 즉시 종료됩니다.\n\n```python\nfor i in range(10):\n    if i == 2:\n        break\n    print(i) # 0, 1 까지만 출력됨\n```\n\n---\n\n### ✏️ 미션\n`for` 문에서 1부터 5까지 반복하다가 `i`가 3이 되면 `break`로 탈출하도록 작성하세요. (결과는 1, 2만 출력)",
                    "initialCode": "for i in range(1, 6):\n    # i가 3일 때 break 하세요\n\n    print(i)\n", "expectedOutput": "1\n2"
                },
                {
                    "id": "c5_l6", "title": "6. 다음 반복으로 건너뛰기 (continue)",
                    "description": "## ⏭️ 이번 건 패스! (continue)\n\n`continue`를 만나면 그 아래의 코드를 실행하지 않고, 다시 반복문의 처음으로 올라가 다음 차례를 진행합니다.\n\n```python\nfor i in range(4):\n    if i == 1:\n        continue\n    print(i) # 0, 2, 3 출력됨\n```\n\n---\n\n### ✏️ 미션\n`1`부터 `4`까지 반복하면서 `2`일 때만 `continue`로 건너뛰어 `1`, `3`, `4`가 한 줄씩 출력되게 하세요.",
                    "initialCode": "for i in range(1, 5):\n    # i가 2일 때 continue 하세요\n\n    print(i)\n", "expectedOutput": "1\n3\n4"
                },
                {
                    "id": "c5_l7", "title": "7. 문자열 순회하기",
                    "description": "## 🔠 문자열도 하나씩!\n\n문자열도 리스트처럼 `for` 문에 넣으면 한 글자씩 꺼내어 쓸 수 있습니다.\n\n```python\nfor char in \"ABC\":\n    print(char)\n# A, B, C 한 줄씩 출력됨\n```\n\n---\n\n### ✏️ 미션\n문자열 `\"HI\"`를 `for` 문으로 돌려 `H`와 `I`를 한 줄씩 출력하세요.",
                    "initialCode": "# for문과 문자열 \"HI\"를 사용하세요\n", "expectedOutput": "H\nI"
                },
                {
                    "id": "c5_l8", "title": "8. 누적 합 구하기",
                    "description": "## ➕ 계속 더하기\n\n반복문을 사용하면 1부터 10까지 더하는 연산도 쉽게 할 수 있습니다. 합을 저장할 변수를 밖에 0으로 준비해야 합니다.\n\n```python\ntotal = 0\nfor i in range(1, 4): # 1, 2, 3\n    total = total + i\nprint(total) # 6\n```\n\n---\n\n### ✏️ 미션\n`1`부터 `5`까지의 모든 수를 더한 결과(`15`)를 `sum_val` 변수에 누적하여 최종값을 출력하세요.",
                    "initialCode": "sum_val = 0\n# 1~5를 더하는 반복문을 작성하세요 (range의 끝값을 주의하세요)\n\nprint(sum_val)\n", "expectedOutput": "15"
                },
                {
                    "id": "c5_l9", "title": "9. 중첩 반복문",
                    "description": "## 🔁 반복문 안의 반복문\n\n시계의 분과 초가 돌아가듯, 반복문 안에 반복문을 넣을 수 있습니다.\n\n```python\nfor i in range(2):\n    for j in range(2):\n        print(i, j)\n```\n\n---\n\n### ✏️ 미션\n외부 `for`는 `1`부터 `2`까지(`i`), 내부 `for`는 `1`부터 `2`까지(`j`) 돌아가게 하여 구구단처럼 `i * j`의 결과를 4번 출력하세요.",
                    "initialCode": "# 중첩 for문을 작성하세요\nfor i in range(1, 3):\n    pass\n", "expectedOutput": "1\n2\n2\n4"
                },
                {
                    "id": "c5_l10", "title": "10. 구구단 만들기",
                    "description": "## ✖️ 2단 출력하기\n\n지금까지 배운 반복문을 응용해 구구단 중 한 단을 출력해봅시다. 문자열 포매팅(f-string)을 쓰면 멋지게 출력할 수 있습니다.\n\n```python\nprint(f\"3 x 1 = {3*1}\")\n```\n\n---\n\n### ✏️ 미션\n반복문을 이용해 2단을 1부터 3까지만 출력하세요. 형식을 맞춰야 통과됩니다.\n(힌트: `print(f\"2 x {i} = {2 * i}\")`)",
                    "initialCode": "# 2단 (2x1, 2x2, 2x3)을 출력하세요\n", "expectedOutput": "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6"
                }
            ]
        },
        {
            "id": "c6",
            "title": "6단원: 함수 (Function)",
            "lessons": [
                {
                    "id": "c6_l1", "title": "1. 함수 정의하기 (def)",
                    "description": "## 🧩 나만의 명령 만들기\n\n자주 쓰는 코드를 하나로 묶어 이름을 붙이는 것을 '함수'라고 합니다. 파이썬에서는 `def` 키워드를 씁니다.\n\n```python\ndef say_hi():\n    print(\"Hi!\")\n\nsay_hi() # 호출\n```\n\n---\n\n### ✏️ 미션\n`\"Hello\"`를 출력하는 `hello()` 함수를 만들고, 그 함수를 한 번 호출하세요.",
                    "initialCode": "# hello 함수를 만들고 호출하세요\n", "expectedOutput": "Hello"
                },
                {
                    "id": "c6_l2", "title": "2. 매개변수 (Parameter)",
                    "description": "## 📥 함수에 값 전달하기\n\n함수 괄호 안에 변수를 만들어두면, 호출할 때 값을 전달받아 사용할 수 있습니다.\n\n```python\ndef greet(name):\n    print(\"안녕 \" + name)\n\ngreet(\"파이썬\") # 안녕 파이썬\n```\n\n---\n\n### ✏️ 미션\n이름을 전달받아 `Hello 이름` 형태로 출력하는 `say_hello(name)` 함수를 만들고, `\"Alice\"`를 전달하여 호출하세요.",
                    "initialCode": "# say_hello 함수를 만들고 \"Alice\"로 호출하세요\n", "expectedOutput": "Hello Alice"
                },
                {
                    "id": "c6_l3", "title": "3. 여러 개의 매개변수",
                    "description": "## 📥 📥 두 개 이상 받기\n\n매개변수를 콤마로 구분하여 여러 개 받을 수도 있습니다.\n\n```python\ndef add_print(a, b):\n    print(a + b)\n\nadd_print(3, 5) # 8\n```\n\n---\n\n### ✏️ 미션\n두 숫자 `x`, `y`를 받아 곱셈 결과를 출력하는 `multiply(x, y)` 함수를 만들고, `4`와 `5`를 넣어 호출하세요.",
                    "initialCode": "# multiply 함수를 만들고 4, 5를 넣어 호출하세요\n", "expectedOutput": "20"
                },
                {
                    "id": "c6_l4", "title": "4. 반환값 (return)",
                    "description": "## 📤 결과 돌려주기 (return)\n\n함수가 계산한 결과를 밖으로 빼내려면 `return` 키워드를 사용합니다. `print`와 `return`은 다릅니다!\n\n```python\ndef add(a, b):\n    return a + b\n\nresult = add(2, 3)\nprint(result) # 5\n```\n\n---\n\n### ✏️ 미션\n어떤 수 `num`을 받아 10을 뺀 값을 `return`하는 `minus_ten(num)` 함수를 만들고, `20`을 넣어 반환된 값을 `print` 하세요.",
                    "initialCode": "# 코드를 완성하세요\n", "expectedOutput": "10"
                },
                {
                    "id": "c6_l5", "title": "5. 디폴트 매개변수",
                    "description": "## 🪹 기본값 설정하기\n\n함수에 값을 전달하지 않았을 때 사용할 기본값을 지정해둘 수 있습니다.\n\n```python\ndef greet(name=\"손님\"):\n    print(\"안녕 \" + name)\n\ngreet()       # 안녕 손님\ngreet(\"철수\") # 안녕 철수\n```\n\n---\n\n### ✏️ 미션\n`say_msg(msg=\"기본메시지\")` 함수를 만드세요. 함수는 msg 값을 그대로 print 합니다. 그 후 괄호를 비운 채로 호출해보세요.",
                    "initialCode": "# 디폴트 매개변수를 사용하여 작성하세요\n", "expectedOutput": "기본메시지"
                },
                {
                    "id": "c6_l6", "title": "6. 전역 변수와 지역 변수",
                    "description": "## 🌍 변수의 활동 범위 (Scope)\n\n함수 안에서 만든 변수(지역 변수)는 함수 밖에서 쓸 수 없습니다. 밖에서 만든 변수(전역 변수)는 안에서도 읽을 수 있습니다.\n\n```python\nmsg = \"Global\" # 전역 변수\ndef test():\n    local_msg = \"Local\" # 지역 변수\n    print(msg)\n```\n\n---\n\n### ✏️ 미션\n함수 외부에 선언된 `x = 100`을 함수 내부에서 `print`하는 `show_x()` 함수를 만들고 호출하세요.",
                    "initialCode": "x = 100\n# show_x 함수를 만들고 호출하세요\n", "expectedOutput": "100"
                },
                {
                    "id": "c6_l7", "title": "7. return으로 함수 끝내기",
                    "description": "## 🛑 중간에 탈출\n\n반복문의 `break`처럼, 함수 안에서 `return`을 만나면 즉시 함수가 종료되고 값을 돌려줍니다.\n\n```python\ndef check(num):\n    if num < 0:\n        return \"음수\"\n    return \"양수\"\n```\n\n---\n\n### ✏️ 미션\n`is_even(n)` 함수를 만드세요. `n`이 짝수(`n % 2 == 0`)이면 `\"짝수\"`를 return하고, 아니면 `\"홀수\"`를 return합니다. `4`를 넣어 출력하세요.",
                    "initialCode": "# is_even 함수를 작성하세요\n", "expectedOutput": "짝수"
                },
                {
                    "id": "c6_l8", "title": "8. 여러 값 반환하기",
                    "description": "## 📦 튜플로 한 번에 여러 개\n\n파이썬은 콤마로 여러 값을 return할 수 있습니다. (사실은 튜플이라는 자료형으로 묶여서 나옵니다)\n\n```python\ndef calc(a, b):\n    return a+b, a-b\n\nres1, res2 = calc(5, 3)\nprint(res1, res2)\n```\n\n---\n\n### ✏️ 미션\n함수 `get_two()`를 만들고 `10`과 `20` 두 개를 return하도록 하세요. 반환된 두 값을 받아 `print()`로 모두 출력하세요.",
                    "initialCode": "# get_two 함수를 작성하세요\n", "expectedOutput": "10 20"
                },
                {
                    "id": "c6_l9", "title": "9. 내장 함수 (Built-in Functions)",
                    "description": "## 🛠️ 이미 만들어진 도구들\n\n파이썬에는 `print()`, `type()`, `len()` 외에도 기본적으로 제공하는 편리한 함수가 많습니다.\n- `max(1, 5, 3)` -> 가장 큰 수 반환\n- `min(1, 5, 3)` -> 가장 작은 수 반환\n\n---\n\n### ✏️ 미션\n`max()` 함수를 사용하여 `10`, `50`, `30` 중에서 가장 큰 값을 구하여 출력하세요.",
                    "initialCode": "# max 함수를 사용하세요\n", "expectedOutput": "50"
                },
                {
                    "id": "c6_l10", "title": "10. 종합 연습: 팩토리얼",
                    "description": "## 🏆 함수 종합 미션\n\n지금까지 배운 반복문, 조건문, 함수를 모두 합쳐서 수학의 팩토리얼(n!)을 구하는 함수를 만들어봅시다.\n예: `4!` = 4 x 3 x 2 x 1 = 24\n\n---\n\n### ✏️ 미션\n숫자 `n`을 받아 1부터 n까지 모두 곱한 값을 `return`하는 `factorial(n)` 함수를 만들고, `factorial(4)`의 결과를 출력하세요.",
                    "initialCode": "def factorial(n):\n    result = 1\n    # 반복문을 사용하여 1부터 n까지 곱하세요\n\n    return result\n\nprint(factorial(4))\n", "expectedOutput": "24"
                }
            ]
        }
    ]
}

with open("default_content.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("default_content.json 파일이 성공적으로 생성되었습니다!")
