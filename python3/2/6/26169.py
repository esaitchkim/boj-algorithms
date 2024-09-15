"""26169.py
Title: 세 번 이내에 사과를 먹자
Url: https://www.acmicpc.net/problem/26169
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write
board = []

for _ in range(5):
    line = [*map(int, input().split())]
    board.append(line)

r, c = map(int, input().split())

stack = [(r, c, 0, 0, [])]
result = 0
while stack:
    t_r, t_c, t_cnt, t_apple, visited = stack.pop()
    if t_apple >= 2:
        result = 1
        break
    if t_cnt > 3:
        continue
    if (t_r, t_c) not in visited:
        if board[t_r][t_c] == 1:
            t_apple += 1
        t_cnt += 1
        if t_r > 0 and board[t_r - 1][t_c] != -1:
            stack.append((t_r - 1, t_c, t_cnt, t_apple, visited + [(t_r, t_c)]))
        if t_r < 4 and board[t_r + 1][t_c] != -1:
            stack.append((t_r + 1, t_c, t_cnt, t_apple, visited + [(t_r, t_c)]))
        if t_c > 0 and board[t_r][t_c - 1] != -1:
            stack.append((t_r, t_c - 1, t_cnt, t_apple, visited + [(t_r, t_c)]))
        if t_c < 4 and board[t_r][t_c + 1] != -1:
            stack.append((t_r, t_c + 1, t_cnt, t_apple, visited + [(t_r, t_c)]))

print(f"{result}\n")
