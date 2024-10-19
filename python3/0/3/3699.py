"""3699.py
Title: Tower Parking
Url: https://www.acmicpc.net/problem/3699
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    h, l = map(int, input().split())
    tower = {}
    for i in range(h):
        initial_placements = [*map(int, input().split())]
        tmp_dict = {
            initial_placements[j]: (i, j) for j in range(len(initial_placements)) if initial_placements[j] != -1
        }
        tower.update(tmp_dict)

    belt = [0 for _ in range(h)]
    elapsed = 0
    for i in range(1, len(tower) + 1):
        car = tower[i]
        elapsed += car[0] * 20
        tmp_move = abs(car[1] - belt[car[0]])
        elapsed += tmp_move * 5 if tmp_move < l - tmp_move else (l - tmp_move) * 5
        belt[car[0]] = car[1]

    print(f"{elapsed}\n")
