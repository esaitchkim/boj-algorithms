"""30031.py
Title: 지폐 세기
Url: https://www.acmicpc.net/problem/30031
"""

import sys

input = sys.stdin.readline

N = int(input())
total = 0
for _ in range(N):
    w, h = map(int, input().split())
    if h == 68:
        if w == 136:
            total += 1000
        elif w == 142:
            total += 5000
        elif w == 148:
            total += 10000
        elif w == 154:
            total += 50000

print(total)
