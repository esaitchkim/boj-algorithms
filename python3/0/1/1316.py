"""1316.py
Title: 그룹 단어 체커
Url: https://www.acmicpc.net/problem/1316
"""

import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    word_set = set()
    checker_flag = True
    before_char = ""
    word = input().rstrip()
    for char in word:
        before_len = len(word_set)
        if char != before_char:
            before_char = char
            word_set.add(char)
            after_len = len(word_set)
            if before_len == after_len:
                checker_flag = False
                break
    if checker_flag:
        cnt += 1

print(cnt)
