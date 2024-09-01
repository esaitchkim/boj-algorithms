"""10874.py
Title: Dr. L's exam
Url: https://www.acmicpc.net/problem/10874
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
for i in range(1, N + 1):
    perfect = True
    answer = [*map(int, input().split())]
    for j in range(len(answer)):
        if answer[j] != (j % 5) + 1:
            perfect = False
            break
    if perfect:
        print(f"{i}\n")
