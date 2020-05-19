# 입력받아 출력하기
name = input('이름: ')
print( name + "씨 방가방가!!")
print( name, "씨 방가방가!!")
print('Hello ', name, '!')
print('Hello ', name, '!', sep='')
print('Hello ', name, '!', sep='-')
print("{}씨 방가방가!!".format(name))
print("'{0}'씨 방가방가!!".format(name))
print("'{name}'씨 방가방가!!".format(name=name))
print("'{0} {0} {0}'씨 방가방가!!".format(name))
print("'{name}'씨 방가방가!!".format(name=name*3))

age = input("나이 : ")
print(age, type(age))

# 문자를 입력해도 에러 아님
age = input("나이 : ")
if age.isdigit():
    age = int(age)
print(age, type(age))

# 문자를 입력하면 에러
age = int(input("나이 : "))
print(age, type(age))