"""25495.py
Title: 에어팟
Url: https://www.acmicpc.net/problem/25495
"""

N = int(input())
A = [*map(int, input().split())]

cnt = 0
battery = 2
consum = 2

bef_dev = A[0]

for dev in A[1:]:
    if dev != bef_dev:
        consum = 2
        battery += consum
    else:
        consum *= 2
        battery += consum

    if battery >= 100:
        bef_dev = 0
        battery = 0
        consum = 2
    else:
        bef_dev = dev

print(battery)
