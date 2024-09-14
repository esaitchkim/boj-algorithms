"""1026.py
Title: 보물
Url: https://www.acmicpc.net/problem/1026
"""

N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

A.sort(reverse=False)
sorted_idx = sorted(range(N), key=lambda i: B[i], reverse=True)

res = [0] * N

for i in range(N):
    res[sorted_idx[i]] = A[i] * B[sorted_idx[i]]
print(sum(res))
