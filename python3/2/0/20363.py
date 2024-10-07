"""20363.py
Title: 당근 키우기
Url: https://www.acmicpc.net/problem/20363
"""

X, Y = map(int, input().split())

if X < Y:
    X, Y = Y, X

X += Y // 10
print(X + Y)
