"""11758.py
Title: CCW
Url: https://www.acmicpc.net/problem/11758
"""

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

res = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

if res == 0:
    print(0)
elif res > 0:
    print(1)
else:
    print(-1)
