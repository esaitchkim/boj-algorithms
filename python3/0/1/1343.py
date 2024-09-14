"""1343.py
Title: 폴리오미노
Url: https://www.acmicpc.net/problem/1343
"""

P1 = "AAAA"
P2 = "BB"

boards = input().split(".")

result_string = ""
flag = True

for board in boards:
    len_board = len(board)
    if len(board) % 2 != 0:
        flag = False
        break

    result_string += P1 * (len_board // len(P1))
    len_board %= len(P1)

    result_string += P2 * (len_board // len(P2))
    result_string += "."

if flag:
    print(result_string[:-1])
else:
    print(-1)
