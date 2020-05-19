# 입력을 받을 수 없을까?
age = input("나이?")
print(age + "살이네 행님이라 불러")

age = input("나이?")  # 입력되면 String이다.
# 에러 : SyntaxError: invalid syntax
# print("내년 나이는 " + age+1 + "살이네 행님이라 불러") 

# 타입이 자동 변환되지 않는다.

# 에러 : TypeError: can only concatenate str (not "int") to str
# print("내년 나이는 " + (age+1) + "살이네 행님이라 불러") 

# 에러 : TypeError: can only concatenate str (not "int") to str
# print("내년 나이는 " + (int(age)+1) + "살이네 행님이라 불러") 

print("내년 나이는 " + str(int(age)+1) + "살이네 행님이라 불러")
