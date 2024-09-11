"""1085.py
Title: 직사각형에서 탈출
Url: https://www.acmicpc.net/problem/1085
"""

x, y, w, h = map(int, input().split())
res = min(x, y, w - x, h - y)
print(res)
