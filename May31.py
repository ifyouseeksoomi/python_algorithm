# n = input()
# n = int(n)
# print(type(n))
# print(n)

import sys
sys.stdin = open("in5.txt", "rt")

nk = input()

n = int(nk.split(' ')[0])
print("n = " + str(n))

k = int(nk.split(' ')[1])  # 4
print("k = " + str(k))

n_divisors = list()

for a in range(1, n+1):
    if (n % a) == 0:
        n_divisors.append(a)
    if a == n:
        break
    else:
        continue

len_of_n_divisors = len(n_divisors)
print("len_of_n_divisors = " + str(len_of_n_divisors))

if len_of_n_divisors < k:
    print("the length of divisors of n is less than k itself: -1")
else:
    print("the Kth divisor of n = " + str(n_divisors[k-1]))
    sys.stdin = open("out5.txt", "rt")
    a = int(input())

    if a == n_divisors[k-1]:
        print('you got it right soome!')
