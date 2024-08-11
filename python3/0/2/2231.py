"""2231.py
Title: 분해합
Url: https://www.acmicpc.net/problem/2231
"""

N = int(input())

gen = 0
digit = len(str(N))

for i in range(max(N - (9 * digit), 0), N):
    n_string = str(i)
    m = i + sum([int(j) for j in n_string])
    if m == N:
        gen = i
        break

print(gen)
