"""6131.py
Title: Perfect Squares
Url: https://www.acmicpc.net/problem/6131
"""

N = int(input())
res = 0

for B in range(1, 501):
    for A in range(B, 501):
        if B * B + N == A * A:
            res += 1
            break
        elif B * B + N < A * A:
            break

print(res)
