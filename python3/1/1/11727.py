"""11727.py
Title: 2×n 타일링 2
Url: https://www.acmicpc.net/problem/11727
"""

n = int(input())
dp = [1] * (n + 1)
for i in range(2, n + 1):
    dp[i] = 2 * dp[i - 2] + dp[i - 1]

print(dp[n] % 10007)
