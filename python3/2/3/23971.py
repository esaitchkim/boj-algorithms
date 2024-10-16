"""23971.py
Title: ZOAC 4
Url: https://www.acmicpc.net/problem/23971
"""

H, W, N, M = map(int, input().split())

res = 0
res += ((W - 1) // (M + 1)) + 1
res *= ((H - 1) // (N + 1)) + 1
print(res)
