# 한번에 여러개 입력하기
i,j,k = input('문자열 3개를 입력하세요: ').split()   # 입력받은 값을 공백을 기준으로 분리
print('i = {0}, j = {1}, k = {2}'.format(i,j,k));

x, y = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
x = int(x)    # 변수를 정수로 변환한 뒤 다시 저장
y = int(y)    # 변수를 정수로 변환한 뒤 다시 저장
print("{0} + {1} = {2}".format(x, y, x + y))

x, y = y, x # 값 교환
print("{0} + {1} = {2}".format(x, y, x + y))

yy, mm, dd = input('생년월일을  ,(콤마)로 구분하여 입력하세요: ').split(",")    # 입력받은 값을 ,(콤마)를 기준으로 분리
print("{0}년 {1}월 {2}일".format(yy, mm, dd))

"""
split의 결과를 매번 int로 변환해주려니 귀찮습니다. 이때는 map 함수를 함께 사용하면 됩니다. 
map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환해줍니다(실수로 변환할 때는 int대신 float를 넣습니다.).

변수, ... = map(int, input().split())
변수, ... = map(int, input().split(기준문자))

map은 뒤에서 자세하게 배웁니다.
"""
x, y = map(int, input('숫자 두 개를 입력하세요: ').split())
print("{0} + {1} = {2}".format(x, y, x + y))

yy, mm, dd = map(str, input('생년월일을  ,(콤마)로 구분하여 입력하세요: ').split(","))    # 입력받은 값을 ,(콤마)를 기준으로 분리
print("{0}년 {1}월 {2}일".format(yy, mm, dd))

"""
input과 split의 결과가 문자열라는 점이 중요합니다. 
따라서 숫자 계산을 한다면 int, float를 사용해서 결과를 숫자로 변환해주어야 한다는 점 기억하세요. 
그리고 split의 결과를 모두 int, float로 변환할 때는 map을 사용하면 편리합니다.
"""