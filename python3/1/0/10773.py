"""10773.py
Title: Zero That Out
Url: https://www.acmicpc.net/problem/10773
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

K = int(input())

num_list = []

for _ in range(K):
    input_integer = int(input())
    if input_integer == 0:
        num_list.pop()
    else:
        num_list.append(input_integer)

sum_integers = sum(num_list)

print(f"{sum_integers}\n")
