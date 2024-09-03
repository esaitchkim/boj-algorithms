"""9251.py
Title: LCS
Url: https://www.acmicpc.net/problem/9251
"""

str1 = " " + input()
str2 = " " + input()

dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(str1) - 1][len(str2) - 1])
