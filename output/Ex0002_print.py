# 출력에 대하여 알아보겠습니다.
# 특수문자 처리하기
print('Hello World!!')
print("Hello World!!")
# 기본 확장 문자(escape sequence) 사용이 가능합니다.
print("Hello \tWorld!!") # \t : 탭
print("Hello \nWorld!!") # \n : 개행
# "(큰따옴표)안에 '(작은따옴표)는 사용 가능합니다.
print("나의 이름은 '한사람'입니다.")
# '(작은따옴표)안에 "(큰따옴표)는 사용 가능합니다.
print('나의 이름은 "한사람"입니다.')
# "(큰따옴표)안에 "(큰따옴표)는 확장 문자(escape sequence)를 사용해야 합니다.
print("나의 이름은 \"한사람\"입니다.")
# '(작은따옴표)안에 '(작은따옴표)는 확장 문자(escape sequence)를 사용해야 합니다.
print('나의 이름은 \'한사람\'입니다.')
# \자체를 출력하기 위해서는 \두개를 연달아 사용합니다.
print('나의 이름은 \\한사람\\입니다.')
# 문자열 * 숫자 : 문자열을 숫자만큼 반복합니다.
print('-' * 50)
# 여러 줄의 내용을 있는 그대로 사용하려면 "(큰따옴표) 세 개를 연달아 사용합니다. 
# 여기서는 주석입니다. 
'''
기본 확장 문자(escape sequence)
\' : 작은따옴표 문자
\" : 큰따옴표 문자
\\ : backslash 문자
\a : bell 문자
\b : backslash 문자
\f : Form feed 문자
\n : new line 문자
\r : carriage return 문자(\n와 동일하지 않다.)
\t : tab 문자
\v : vertical tab 문자
'''