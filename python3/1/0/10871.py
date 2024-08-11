"""10871.py
Title: X보다 작은 수
Url: https://www.acmicpc.net/problem/10871
"""

N, X = map(int, input().split())

A = map(int, input().split())

result = []
for num in A:
    if num < X:
        result.append(num)

print(*result, sep=" ")
