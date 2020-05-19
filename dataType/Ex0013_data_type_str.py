# food = 'Python's favorite food is perl'
# 문자열을 저장할때는 따옴표의 쌍을 맞추면 에러가 아니다.
food = "Python's favorite food is perl"
print(food)
food = 'Python"s favorite food is perl'
print(food)
food = "Python\"s favorite food is perl"
print(food)
food = 'Python\'s favorite food is perl'
print(food)

string = """재미있는 파이선
이렇게 유연하다니
정말 좋구나
"""
print(type(string))
print(string)

string = '''
재미있는 파이선
이렇게 유연하다니
정말 좋구나
'''
print(type(string))
print(string)


# \ 는 다음 줄과  연결된 문장이라는 표시이다.
string = '재미있는 파이선' + '\n' + \
"이렇게 유연하다니" + '\n' + \
"정말 좋구나"

print(type(string))
print(string)

data = 10 + \
       20 + \
       30
print(type(data))
print(data)
