"""15650.py
Title: N과 M (2)
Url: https://www.acmicpc.net/problem/15650
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())


def back_tracking(N, M, start=1, stack=[]):
    if len(stack) == M:
        yield stack
        return

    for i in range(start, N + 1):
        yield from back_tracking(N, M, i + 1, stack + [i])


for res in back_tracking(N, M):
    print(" ".join(map(str, res)) + "\n")
