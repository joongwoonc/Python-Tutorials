# 숫자만  입력
while True:
    age = input("나이 : ")
    if age.isdigit():
        age = int(age)
        break

next_age = age + 1
print("내년 나이는 ", end="") # end는 마지막 처리를 어떻게 할것인가? 기본값은 "\n"이다.
print(next_age, end="")
print("살이네 행님이라 불러")

# 연령대를 알아볼까?
print(str(age/10*10) + "대입니다.") # 정수/정수 = 실수 : /(나누기)연산자 주의를 해야 한다.
# 헐~~~~ 그럼 어떻게?
print(str(age//10*10) + "대입니다.") # //는 정수몫을 구한다. 몫을 넘지 않는 최대 정수를 구한다.

# 3항 연산자
# 참 if 조건 else 거짓
print(age, "살은 ", age//10*10,"대 ", "후반" if age%10>5 else "초반","입니다", sep="")
# and 와 or를 이용한 3항 연산
print(age, "살은 ", age//10*10,"대 ", age%10>5 and "후반" or "초반","입니다", sep="")


# 결과를 꼭 확인해 봐라~~~
print(10/3)
print(10//3)
print(-10/3)
print(-10//3)