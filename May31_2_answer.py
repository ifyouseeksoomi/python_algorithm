import sys
sys.stdin = open("in1.txt", "rt")
# 'rt' is now synonym of 'r' ('t' usually stands for 'text mode' as default)
# stdin is used for all interactive input (including calls to input())

T = int(input())  # 케이스의 개수

for t in range(T):  # 케이스만큼 룹을 돈다
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print(f'#{t+1} {a[k-1]}')
