"""9095.py
Title: Adding 1s, 2s, and 3s
Url: https://www.acmicpc.net/problem/9095
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

dp = [1] * 11
dp[2] = 2
for i in range(3, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(T):
    n = int(input())
    print(f"{dp[n]}\n")
