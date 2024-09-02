"""9465.py
Title: Stickers
Url: https://www.acmicpc.net/problem/9465
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = []
    dp = [[0 for _ in range(n)] for _ in range(2)]
    line = [*map(int, input().split())]
    stickers.append(line)
    line = [*map(int, input().split())]
    stickers.append(line)

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if n >= 2:
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + stickers[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i]

    print(f"{max(dp[0][n-1], dp[1][n-1])}\n")
