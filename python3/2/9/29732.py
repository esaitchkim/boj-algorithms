"""29732.py
Title: Rick-Roll Virus
Url: https://www.acmicpc.net/problem/29732
"""

N, M, K = map(int, input().split())
S = input()
infected = [1 if ch == "R" else 0 for ch in S]

for i in [x for x in range(N) if infected[x] == 1]:
    left, right = max(0, i - K), min(N, i + K + 1)
    infected[left:right] = [1 for _ in range(right - left)]

res = sum(infected)

if res <= M:
    print("Yes")
else:
    print("No")
