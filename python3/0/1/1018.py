"""1018.py
Title: 체스판 다시 칠하기
Url: https://www.acmicpc.net/problem/1018
"""

import sys

input = sys.stdin.readline


def check_board(board: list, black_first: list, white_first: list):
    """체스판을 비교하여 다시 칠해야하는 칸의 수를 계산함.

    Args:
        board (list): 주어진 체스판(8 by 8)
        black_first (list): 검정이 먼저오는 체스판(8 by 8)
        white_first (list): 하양이 먼저오는 체스판(8 by 8)

    Returns:
        _type_: _description_
    """
    repaint_black = 0
    repaint_white = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != black_first[i][j]:
                repaint_black += 1
            if board[i][j] != white_first[i][j]:
                repaint_white += 1

    result = min(repaint_black, repaint_white)

    return result


black_first = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
]

white_first = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
]

N, M = map(int, input().split())
board = list()

for _ in range(N):
    lines = list(input().rstrip())
    board.append(lines)

min_repaint_cnt = 64

for i in range(N - 7):
    for j in range(M - 7):
        sub_board = [row[j : j + 8] for row in board[i : i + 9]]
        tmp_cnt = check_board(sub_board, black_first, white_first)
        min_repaint_cnt = min(min_repaint_cnt, tmp_cnt)
        if min_repaint_cnt == 0:
            break
    if min_repaint_cnt == 0:
        break

print(min_repaint_cnt)
