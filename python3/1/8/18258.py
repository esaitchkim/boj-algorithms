"""18258.py
Title: 큐 2
Url: https://www.acmicpc.net/problem/18258
"""

from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

queue = deque()

N = int(input())
for _ in range(N):
    input_strings = input().rstrip().split()

    if input_strings[0] == "push":
        queue.append(int(input_strings[1]))
    elif input_strings[0] == "pop":
        if queue:
            print(f"{queue.popleft()}\n")
        else:
            print("-1\n")
    elif input_strings[0] == "size":
        print(f"{len(queue)}\n")
    elif input_strings[0] == "empty":
        if queue:
            print("0\n")
        else:
            print("1\n")
    elif input_strings[0] == "front":
        if queue:
            print(f"{queue[0]}\n")
        else:
            print("-1\n")
    elif input_strings[0] == "back":
        if queue:
            print(f"{queue[-1]}\n")
        else:
            print("-1\n")
