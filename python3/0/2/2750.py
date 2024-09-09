"""2750.py
Title: 수 정렬하기
Url: https://www.acmicpc.net/problem/2750
"""

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
print = sys.stdout.write


N = int(input())

heap = []

for _ in range(N):
    num = int(input())
    heappush(heap, num)

while heap:
    num = heappop(heap)
    print(f"{num}\n")
