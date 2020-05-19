import sys # 모듈을 읽어들인다.
print(sys.version)

data = input("정수 입력 : ")
# 데이터의 타입을 알아내기 위해서는 type 클래스를 이용한다.
print(data, type(data))

# eval 함수는 가장 적합한 자료형으로 변환해 준다.
data = eval(input("정수 입력 : "))
print(data, type(data))
# 2진수로 입력
data = int(input("정수 입력(2진수) : "), 2)
print(data, type(data))

# 8진수로 입력
data = int(input("정수 입력(8진수) : "), 8)
print(data, type(data))

# 10진수로 입력
data = int(input("정수 입력(10진수) : "), 10)
print(data, type(data))

# 16진수로 입력
data = int(input("정수 입력(16진수) : "), 16)
print(data, type(data))

colors = input("값을 다음과 같이 입력 ['red','green','blue'] : ")
print(colors, type(colors))

colors = eval(input("값을 다음과 같이 입력 ['red','green','blue'] : "))
print(colors, type(colors)) # list

colors = eval(input("값을 다음과 같이 입력 ('red','green','blue') : "))
print(colors, type(colors)) # tuple