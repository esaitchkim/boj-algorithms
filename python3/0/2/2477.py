"""2477.py
Title: 참외밭
Url: https://www.acmicpc.net/problem/2477
"""

K = int(input())
x_arr = []
y_arr = []
x, y, area = 0, 0, 0

for _ in range(6):
    d, l = map(int, input().split())
    if d == 1:
        x += l
    elif d == 2:
        x -= l
    elif d == 3:
        y -= l
    elif d == 4:
        y += l

    x_arr.append(x)
    y_arr.append(y)

x_arr.append(x_arr[0])
y_arr.append(y_arr[0])

for i in range(6):
    area += x_arr[i] * y_arr[i + 1]
    area -= y_arr[i] * x_arr[i + 1]

area = abs(area) // 2
res = area * K
print(res)
