# 중첩 반복문 (2중 포문)
'''
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
'''

# 문자열과 내장함수
import random as r
msg = "It is Time"
# print(msg.upper()) # 궁금 msg.upper() vs. upper(msg)

'''
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))  # 찾아서 가장 첫번째 인덱스 번호를 리턴
print(tmp.count('T'))
print(tmp[:2])
print(msg[3:5])
'''

'''
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()
'''

# 공백 삭제하기 (알파벳인 경우에만 출력) : isalpha()
'''
for x in msg:
    if x.isalpha():
        print(x, end='')
'''

# 아스키 넘버와 실제 문자 스왑 : ord(), chr()
'''
for x in msg:
    print(ord(x), end=' ')

tmp = 65
print(chr(tmp))
'''

# 리스트와 내장함수(1)
'''
a = [1, 2, 3, 4, 5]  # a = list() 와 같음
b = list(range(1, 11))
# c = list(2, 3, 4) 는 불가 list 함수는 argument 1개만 받음
d = a+b
# print(d)

# append(), insert(), pop(), remove(), index()
# pop은 인덱스 기반, remove는 밸류 기반
# sum(), max(), min()

# shuffle()
print(a)
e = r.shuffle(a)  # mutable
# shuffle 함수는 return 값이 없이 그냥 원본을 수정하기만 함 : mutable한 성질을 가지는 shuffle 함수는 리턴하는 값이 따로 없음
print(a)
print(e)  # 그래서 여기가 None

# sort
print(a)
a.sort()  # sort 함수 역시 return 값이 없이 원본을 수정함
print(a)
f = sorted(a)
print(f)  # sorted의 경우 오름차순으로 재배열하여 새로운 값 리턴
# 결론 : sort는 뮤터블한 리스트 내장함수, sorted는 이뮤터블 (하는 일은 동일)

g = f.pop()
print(g)
print(f)
# pop도 원본에 변형을 일으키므로 뮤터블한 함수, 그리고 리턴 값도 존재(인자 전달하지 않을 경우 맨 마지막 엘리먼트를 remove)

h = f.remove(1)
print(h)  # None. remove 함수도 리턴 값이 없음
print(f) # 또한 remove 역시 원본 리스트 값에 변형을 주므로 뮤터블

# clear() : 리스트 내 모든 값 삭제하기
'''

# enumerate: 인덱스 번호와 밸류 동시 출력
'''
a = [1, 2, 3, 4, 5]
for x in enumerate(a):
    print(x)  # 튜플의 형태로 리턴(ex. (0, 1))

for x in enumerate(a):
    print(x[0], x[1])

for i, v in enumerate(a):
    print(i, v)

# all()
if all(60 > x for x in a):
    print("올 참")
else:
    print("참 아닌 것이 있음")
# all()함수에 인자로 넘기는 식이 모-두 참일 때만 참, 하나라도 아니면 거짓

# any()
if any(60  > x for x in a):
    print("모두가 참은 아님, 단 하나라도 참이 있음")

else:
    print("참 하나도 없음")
'''

# 2차원 리스트 생성
'''
# a = [0]*3
# print(a)
a = [[0]*3 for _ in range(3)]
# print(a)
a[0][1] = 3
# print(a)

for x in a:
    for y in x:
        print(y)
    print()
'''

# 함수 만들기
'''
def add(a, b):
    c = a + b
    return c

add(3, 2)
'''

'''
def calc(a, b):
    c = a+b
    d = a*b
    return c, d # 리턴 값이 두개일 때는 튜플 형태로 리턴

print(calc(5, 6))
'''

# 소수만 건져내는 함수 만들어보기
'''
a = [1, 4, 5, 7, 8]

def isPrime(x):
    if x == 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

for y in a:
    if isPrime(y):
        print(y, end=' ')
'''

# 람다 함수 (익명의 함수, 람다 표현식)


def plus_two(x): return x+2


a = [1, 2, 3]
print(list(map(plus_two, a)))
print(list(map(lambda x: x*2, a)))


# sorted 내장 함수에 람다식 사용해보기
students = [
    ('홍길동', 3.9, 2016304),
    ('박철수', 3.0, 2016301),
    ('김영희', 4.3, 2016303)
]

new = sorted(students, key=lambda student: student[2])
print(new)
