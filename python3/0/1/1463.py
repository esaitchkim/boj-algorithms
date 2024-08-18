"""1463.py
Title: 1로 만들기
Url: https://www.acmicpc.net/problem/1463
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

dp = [0] * (N + 1)

if N >= 2:
    dp[2] = 1

if N >= 3:
    dp[3] = 1

for i in range(4, N + 1):
    dp[i] = dp[i - 1]
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2])
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3])
    dp[i] += 1

print(f"{dp[N]}\n")
