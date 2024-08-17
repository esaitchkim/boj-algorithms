"""1654.py
Title: 랜선 자르기
Url: https://www.acmicpc.net/problem/1654
"""

import sys

input = sys.stdin.readline

K, N = map(int, input().split())
total_cm = 0
cables = {}
for _ in range(K):
    cable = int(input())
    if cables.get(cable) is None:
        cables[cable] = 1
    else:
        cables[cable] += 1

max_cm = max(cables.keys())
min_cm = 1
res_cm = 1

while max_cm >= min_cm:
    now_cm = (min_cm + max_cm) // 2
    lan_cnt = sum((cable // now_cm) * cables[cable] for cable in cables.keys())
    if lan_cnt >= N:
        res_cm = now_cm
        min_cm = now_cm + 1
    else:
        max_cm = now_cm - 1

print(res_cm)
