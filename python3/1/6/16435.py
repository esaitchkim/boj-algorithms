"""16435.py
Title: 스네이크버드
Url: https://www.acmicpc.net/problem/16435
"""

N, L = map(int, input().split())
hi = sorted(map(int, input().split()))

for num in hi:
    if L >= num:
        L += 1
    else:
        break

print(L)
