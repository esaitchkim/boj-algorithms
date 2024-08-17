"""18110.py
Title: solved.ac
Url: https://www.acmicpc.net/problem/18110
"""

import sys

input = sys.stdin.readline

res = 0
difficult_dict = {x: 0 for x in range(1, 31)}

n = int(input())
up_15 = down_15 = int((n * 0.15) + 0.5)

for _ in range(n):
    input_number = int(input())
    difficult_dict[input_number] += 1
    res += input_number

n -= up_15 + down_15
for i in range(30, 0, -1):
    if up_15 > difficult_dict[i]:
        up_15 -= difficult_dict[i]
        res -= difficult_dict[i] * i
        difficult_dict[i] = 0

    else:
        difficult_dict[i] -= up_15
        res -= i * up_15
        break

for i in range(1, 31):
    if down_15 > difficult_dict[i]:
        down_15 -= difficult_dict[i]
        res -= difficult_dict[i] * i
        difficult_dict[i] = 0
    else:
        difficult_dict[i] -= down_15
        res -= i * down_15
        break

if res == 0:
    print(0)
else:
    print(int((res / n) + 0.5))
