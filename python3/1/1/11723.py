"""11723.py
Title: 집합
Url: https://www.acmicpc.net/problem/11723
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

S = [False for _ in range(21)]

M = int(input())

for _ in range(M):
    input_string = input().rstrip().split()

    if input_string[0] == "add":
        S[int(input_string[1])] = True
    elif input_string[0] == "remove":
        S[int(input_string[1])] = False
    elif input_string[0] == "check":
        print(f"{1 if S[int(input_string[1])] else 0}\n")
    elif input_string[0] == "toggle":
        S[int(input_string[1])] = not S[int(input_string[1])]
    elif input_string[0] == "all":
        S = [True for _ in range(21)]
    elif input_string[0] == "empty":
        S = [False for _ in range(21)]
