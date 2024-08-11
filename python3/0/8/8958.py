"""8958.py
Title: OX퀴즈
Url: https://www.acmicpc.net/problem/8958
"""

test_case = int(input())

for _ in range(test_case):
    ox = input()
    score = 0
    now_point = 0
    for s in ox:
        if s == "O":
            now_point += 1
            score += now_point
        else:
            now_point = 0

    print(score)
