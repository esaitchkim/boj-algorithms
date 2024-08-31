"""25304.py
Title: 영수증
Url: https://www.acmicpc.net/problem/25304
"""

import sys

input = sys.stdin.readline

X = int(input())
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    X -= a * b

if X == 0:
    print("Yes")
else:
    print("No")
