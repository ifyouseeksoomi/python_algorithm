# 대소문자 구분
'''
a = 1
print(a)
A = 3
print(A)
print(a, A)
'''

# 한줄 주석
'''
여러줄 주석
'''

# 할당
'''
a, b, c = 3, 2, 1
print(a, b, c)
# 기존 a 공간에 1을 할당했었으나, 방금 3으로 할당이 새로 되었음
'''

# 값 교환
'''
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)
'''

# 변수 타입
'''
a = 1234566778
print(a)
a = 12.1234235346457
print(a)
print(type(a))
'''

# 출력 옵션
'''
a=1
b=2
print(a, b, sep='')
print(a, b, sep='\n')
print(a, b, sep='^', end='wow\n')
print(f"{a}, {b}")
print("{a}과 {b}를 출력하는 것".format(a=10, b=20))
'''

# 변수 입력과 연산자
'''
a = input("숫자를 입력하세요: ")
print(a)
print(type(a))
a = int(a)
print(type(a))

a, b = input("뭔가를 입력하세요: ").split()
print(a, b)
'''

# map 이용하여 연산해보기
'''
a, b = map(int, input("두 개 숫자를 따로 입력: ").split())
print(a+b)
print(a/b)
print(a//b)  # 몫
print(a % b)  # 나머지
print(a ** b)  # 거듭제곱
'''

# if
'''
x = 7
if 0 < x < 10:
    print("x는 10이하의 자연수")
'''

# if 2
'''
x = 93
if x >= 93:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
'''

# 반복문 기본
'''
a = range(10)
print(list(a))
a = range(1, 11)
print(list(a))

for i in range(10, 0, -1):
    print(i, end=' '본
'''

# 반복문 for-else
'''
for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:
    print(11)
# for문은 조건상 break문에 걸려 비정상 종료되지 않고 else문까지 출력함

for i in range(1, 100):
    print(i, end='')
    if i >= 12:
        break
print('12 이하의 자연수만 출력하였습니다.')
'''

# 반복문 문제 풀기
# 1. 1부터 N까지 홀수 출력하기 (N은 인풋으로 입력받음)
'''
n = int(input('n: '))
for i in range(1, n+1):
    if i % 2 == 0:
        continue
    else:
        print(i)
'''
# 여기서 질문! 위에서 else문 굳이 안쓰는게 더 효율이 좋나?

# 2. 1부터 N까지의 합 구하기 (N은 인풋으로 입력받음)
'''
n = int(input('아무 n이나 입력하시오: '))
a = []
for i in range(n+1):
    a.append(i)
result = sum(a)
print(result)
'''

# 3. N의 약수 출력하기 (N은 인풋으로 입력받음)
'''
n = int(input("또 아무거나 입력하시오: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
    else:
        continue
'''
