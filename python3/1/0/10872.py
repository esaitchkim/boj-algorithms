"""10872.py
Title: 팩토리얼
Url: https://www.acmicpc.net/problem/10872
"""

N = int(input())

res = 1
for i in range(N, 0, -1):
    res *= i

print(res)
