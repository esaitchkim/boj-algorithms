"""2010.py
Title: Electrical Outlets
Url: https://www.acmicpc.net/problem/2010
"""

import sys

input = sys.stdin.readline


K = int(input())
res = 1
for _ in range(K):
    res += int(input())

res -= K
print(res)
