"""2467.py
Title: 용액
Url: https://www.acmicpc.net/problem/2467
"""

N = int(input())

min_value = 2000000001
liq = [*map(int, input().split())]
liq1, liq2 = None, None

if liq[0] * liq[-1] >= 0:
    if liq[0] >= 0:
        print(liq[0], liq[1], sep=" ")
    else:
        print(liq[-2], liq[-1], sep=" ")
else:
    start, end = 0, N - 1
    while start < end:
        res = liq[start] + liq[end]
        if abs(res) <= min_value:
            min_value = abs(res)
            liq1, liq2 = liq[start], liq[end]
        if res == 0:
            break
        elif res < 0:
            start += 1
        else:
            end -= 1
    print(liq1, liq2, sep=" ")
