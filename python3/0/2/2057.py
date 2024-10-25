"""2057.py
Title: 팩토리얼 분해
Url: https://www.acmicpc.net/problem/2057
"""

MAX_N = 1_000_000_000_000_000_000


def factorial(n):
    res = 1
    i = 0
    while True:
        if i > 0:
            res *= i
        if res > n:
            break
        yield res
        i += 1


fac_res = [i for i in factorial(MAX_N)]
fac_res.sort(reverse=True)

N = int(input())

res = 0
for num in fac_res:
    if res + num == N:
        res += num
        break
    elif res + num < N:
        res += num

if res == N and N != 0:
    print("YES")
else:
    print("NO")
