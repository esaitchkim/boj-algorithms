"""26145.py
Title: 출제비 재분배
Url: https://www.acmicpc.net/problem/26145
"""

N, M = map(int, input().split())
S = [*map(int, input().split())] + [0 for _ in range(M)]

for i in range(N):
    T = [*map(int, input().split())]
    S = [S[j] + T[j] for j in range(N + M)]
    S[i] -= sum(T)

print(*S, sep=" ")
