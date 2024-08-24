"""15663.py
Title: N과 M (9)
Url: https://www.acmicpc.net/problem/15663
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
num_list = sorted(map(int, input().split()))
used = [False] * N


def back_tracking(num_list, M, used, stack=[]):
    if len(stack) == M:
        yield stack
        return

    for i in range(len(num_list)):
        if used[i]:
            continue

        if i > 0 and num_list[i] == num_list[i - 1] and not used[i - 1]:
            continue

        used[i] = True
        yield from back_tracking(num_list, M, used, stack + [num_list[i]])
        used[i] = False


for res in back_tracking(num_list, M, used):
    print(" ".join(map(str, res)) + "\n")
