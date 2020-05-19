# 출력에 대하여 알아보겠습니다.
# 여러개 출력하기
print(1,2,3,4)
print(1,2,3,4, sep="-"*5) # 구분자 지정(기본값 공백)
print(1,2,3,4, sep=", ", end="\n\n") # 종료문자 지정(기본값 \n)
# 3개 문장을 3줄로 출력
print("Python")
print("is")
print("Good")
# 3개 문장을 1줄로 출력 
print("Python", end=" ")
print("is", end=" ")
print("Good", end="!"*3+"\n")
a = 100
b = 200
print(a,"+",b,"=",a+b)
