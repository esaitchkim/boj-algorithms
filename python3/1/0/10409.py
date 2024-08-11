"""10409.py
Title: 서버
Url: https://www.acmicpc.net/problem/10409
"""

n, T = map(int, input().split())
jobs = map(int, input().split())

processed = 0

for job in jobs:
    T -= job
    if T >= 0:
        processed += 1
    else:
        break

print(processed)
