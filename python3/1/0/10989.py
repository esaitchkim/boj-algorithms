"""10989.py
Title: 수 정렬하기 3
Url: https://www.acmicpc.net/problem/10989
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

number_list = [0 for _ in range(10001)]
total_cnt = 0
cnt = 0
for _ in range(N):
    number = int(input())
    number_list[number] += 1

for i in range(10001):
    if number_list[i] > 0:
        for j in range(number_list[i]):
            print(f"{i}\n")
