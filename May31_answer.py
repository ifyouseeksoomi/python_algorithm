import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())  # 할당 시 n, k 동시할당하기 & map 함수 사용하기
cnt = 0

for i in range(1, n+1):
    if n % i == 0:  # 이 i가 n의 약수라면
        cnt += 1  # cnt 1 증가시킴
    if cnt == k:  # 약수가 발견될 때마다 1씩 증가시킨 cnt와 k가 같다 == k번째 약수가 발견되었다면,
        print(i)  # 바로 그 i를 출력하고
        break  # 포문 정리
else:
    # for-else 구문에서 else가 돌았다 == for문이 정상 종료되었으나(break 안 탔으나) i를 찾지 못했다 즉 약수 발견이 안됐다
    print(-1)
