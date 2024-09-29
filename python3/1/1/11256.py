"""11256.py
Title: Jelly Bean
Url: https://www.acmicpc.net/problem/11256
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    box_dict = {}
    box_cnt = 0
    for _ in range(N):
        Ri, Ci = map(int, input().split())
        if box_dict.get(Ri * Ci) is None:
            box_dict[Ri * Ci] = 1
        else:
            box_dict[Ri * Ci] += 1
    box_sizes = [*box_dict.keys()]
    box_sizes.sort(reverse=True)
    for size in box_sizes:
        if J > size * box_dict[size]:
            J -= size * box_dict[size]
            box_cnt += box_dict[size]
        else:
            box_cnt += J // size
            if J % size != 0:
                box_cnt += 1
            break
    print(f"{box_cnt}\n")
