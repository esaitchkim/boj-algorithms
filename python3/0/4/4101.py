"""4101.py
Title: Which is Greater?
Url: https://www.acmicpc.net/problem/4101
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

while True:
    num1, num2 = map(int, input().split())
    if num1 == num2 == 0:
        break
    print("Yes\n") if num1 > num2 else print("No\n")
