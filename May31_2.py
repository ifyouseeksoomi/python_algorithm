import sys
sys.stdin = open("in1.txt", "rt")

text_by_line = int(input())

for i in range(text_by_line):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()[s-1:e]))
    a.sort()
    print(a[k-1])
    print(f'#{i+1} {a[k-1]}')
