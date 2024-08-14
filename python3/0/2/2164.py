"""2164.py
Title: 카드2
Url: https://www.acmicpc.net/problem/2164
"""

N = int(input())

num = 1
while num * 2 <= N:
    num *= 2

if num == N:
    result = num
else:
    N -= num
    result = max(1, 2 * N)

print(result)
