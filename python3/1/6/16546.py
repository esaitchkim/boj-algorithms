"""16546.py
Title: Missing Runners
Url: https://www.acmicpc.net/problem/16546
"""

N = int(input())
di = map(int, input().split())
all_runners = N * (N + 1) // 2
finished_runners = sum(di)
res = all_runners - finished_runners
print(res)
