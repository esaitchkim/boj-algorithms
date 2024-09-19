"""15818.py
Title: 오버플로우와 모듈러
Url: https://www.acmicpc.net/problem/15818
"""

N, M = map(int, input().split())
a = map(int, input().split())

res = 1

for num in a:
    res = ((res % M) * (num % M)) % M

print(res)
