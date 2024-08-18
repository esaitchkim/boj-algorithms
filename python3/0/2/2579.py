"""2579.py
Title: 계단 오르기
Url: https://www.acmicpc.net/problem/2579
"""

import sys

input = sys.stdin.readline

n = int(input())
stairs = []
for _ in range(n):
    input_point = int(input())
    stairs.append(input_point)

dp = [i for i in stairs]
if n >= 2:
    dp[1] += dp[0]
if n >= 3:
    dp[2] += max(dp[0], stairs[1])

for i in range(3, n):
    dp[i] += max(dp[i - 3] + stairs[i - 1], dp[i - 2])

print(dp[n - 1])
