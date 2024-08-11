"""4153.py
Title: 직각삼각형
Url: https://www.acmicpc.net/problem/4153
"""

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    a *= a
    b *= b
    c *= c

    max_side = max(a, b, c)
    if a + b + c - (2 * max_side) == 0:
        print("right")
    else:
        print("wrong")
