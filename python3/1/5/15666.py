"""15666.py
Title: N과 M (12)
Url: https://www.acmicpc.net/problem/15666
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
num_list = sorted(set(map(int, input().split())))


def back_tracking(num_list, M, start=0, stack=[]):
    if len(stack) == M:
        yield stack
        return

    for i in range(start, len(num_list)):
        yield from back_tracking(num_list, M, i, stack + [num_list[i]])


for res in back_tracking(num_list, M):
    print(" ".join(map(str, res)) + "\n")
