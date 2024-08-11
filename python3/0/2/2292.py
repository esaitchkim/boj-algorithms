"""2292.py
Title: 벌집
Url: https://www.acmicpc.net/problem/2292
"""

N = int(input())

max_room = 1
i = 1

while True:
    if max_room >= N:
        print(i)
        break

    max_room += 6 * i
    i += 1
