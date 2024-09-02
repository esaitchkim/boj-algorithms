"""2096.py
Title: 내려가기
Url: https://www.acmicpc.net/problem/2096
"""

import sys

input = sys.stdin.readline

N = int(input())
MA, MB, MC = 0, 0, 0
mA, mB, mC = 0, 0, 0

for _ in range(N):
    A, B, C = map(int, input().split())
    MA, MB, MC = max(MA, MB) + A, max(MA, MB, MC) + B, max(MB, MC) + C
    mA, mB, mC = min(mA, mB) + A, min(mA, mB, mC) + B, min(mB, mC) + C

print(max(MA, MB, MC), min(mA, mB, mC))
