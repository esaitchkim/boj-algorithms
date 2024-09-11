"""26546.py
Title: Reverse
Url: https://www.acmicpc.net/problem/26546
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

for _ in range(n):
    input_string, start, end = input().rstrip().split()
    start, end = int(start), int(end)
    result_string = input_string[:start] + input_string[end:]
    print(result_string + "\n")
