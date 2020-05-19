# 출력에 대하여 알아보겠습니다.
# 숫자 형식 (8진법과 16진법) 확장 문자(escape sequence)들과 Unicode 확장 문자(escape sequence)들
# 8진수 또는 16진수 확장 문자(escape sequence)를 사용하여 ASCII 문자를 포함시킬 수 있다. 
# 8진수 확장 문자(escape sequence)는 backslash(\)와 세 자릿수 8진수 숫자를 사용한다. 
# 결과로는 8진수 확장 문자(escape sequence)에 해당하는 ASCII 문자가 출력된다. 
# 16진수 확장 문자(escape sequence)도 이와 비슷하지만 “\”가 아니라 “\x”로 시작되며 16진수 숫자로 구성되는 점이 다르다. 
# 이 확장 문자(escape sequence)는 문자가 더 이상 16진수가 아닐 때 종료된다. 

# 아래의 3개 문장은 모두 'A'을 출력합니다. 
# 문자 A는 ASCII 문자표에서 십진수 값 65이다. 이는 8진수로 하면 101이며 16진수로 하면 41 이다.
print('A')
print('\101')
print('\x41')
# 아래의 3개 문장은 모두 ASCII 10번을 출력합니다. 개행이 나타납니다.
print('\n')
print('\012')
print('\x0A')
'''
Python 3 내의 모든 문자열은 Unicode 문자열(string)이므로 모든 language에서 사용 가능한 대부분의 문자를 포함할 수 있다. 
여기에서 설명하지는 않지만 다음 예제는 위에서 설명한 숫자 형식이나 Unicode 명으로 Unicode 문자를 
escape할 수도 있다는 것을 보여준다.
'''
unicode_a = '\N{LATIN SMALL LETTER A}'  # Unicode 명으로 escape
print(unicode_a) # a
unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'  # Unicode 명으로 escape
print(unicode_a_with_acute) # á