"""17286.py
Title: 유미
Url: https://www.acmicpc.net/problem/17286
"""

x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

d01 = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
d02 = ((x2 - x0) ** 2 + (y2 - y0) ** 2) ** 0.5
d03 = ((x3 - x0) ** 2 + (y3 - y0) ** 2) ** 0.5

d12 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
d13 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
d23 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5

res = int(min(d01 + min(d12, d13) + d23, d02 + min(d12, d23) + d13, d03 + min(d13, d23) + d12))
print(res)
