"""9612.py
Title: Maximum Word Frequency
Url: https://www.acmicpc.net/problem/9612
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
words = {}
for _ in range(n):
    word = input().rstrip()
    if words.get(word) is None:
        words[word] = 1
    else:
        words[word] += 1

words_sort = sorted(words.items(), key=lambda item: (item[1], item[0]), reverse=True)
print(f"{words_sort[0][0]} {words_sort[0][1]}\n")
