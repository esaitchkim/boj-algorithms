"""1931.py
Title: 회의실 배정
Url: https://www.acmicpc.net/problem/1931
"""

import sys

input = sys.stdin.readline

N = int(input())
meeting_list = [[*map(int, input().split())] for _ in range(N)]
meeting_list.sort(key=lambda x: (x[1], x[0]))

last_time = 0
res_cnt = 0
for start_time, end_time in meeting_list:
    if last_time <= start_time:
        res_cnt += 1
        last_time = end_time

print(res_cnt)
