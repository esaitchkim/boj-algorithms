"""14038.py
Title: Tournament Selection
Url: https://www.acmicpc.net/problem/14038
"""

win_count = 0
group = -1
for _ in range(6):
    game_result = input()
    if game_result == "W":
        win_count += 1

if win_count >= 5:
    group = 1
elif win_count >= 3:
    group = 2
elif win_count >= 1:
    group = 3

print(group)
