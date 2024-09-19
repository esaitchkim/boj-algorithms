"""17874.py
Title: Piece of Cake!
Url: https://www.acmicpc.net/problem/17874
"""

n, h, v = map(int, input().split())
THICK = 4

max_h = max(h, n - h)
max_v = max(v, n - v)

vol = max_h * max_v * THICK
print(vol)
