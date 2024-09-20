"""2851.py
Title: GLJIVE
Url: https://www.acmicpc.net/problem/2851
"""

GOAL = 100
NUM_OF_LINES = 10

score = 0
interrup_flag = True
for _ in range(NUM_OF_LINES):
    point = int(input())
    before_score = score
    after_score = score + point

    if interrup_flag:
        if abs(GOAL - before_score) >= abs(GOAL - after_score):
            score = after_score
        else:
            interrup_flag = False
print(score)
