"""10828.py
Title: 스택
Url: https://www.acmicpc.net/problem/10828
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, X):
        self.stack.append(X)

    def pop(self):
        print(f"{self.stack.pop() if len(self.stack)>0 else -1}\n")

    def size(self):
        print(f"{len(self.stack)}\n")

    def empty(self):
        print(f"{1 if len(self.stack)==0 else 0}\n")

    def top(self):
        print(f"{self.stack[-1] if len(self.stack)>0 else -1}\n")


N = int(input())
stack = Stack()
for _ in range(N):
    input_strings = input().rstrip().split()
    if input_strings[0] == "push":
        stack.push(input_strings[1])
    elif input_strings[0] == "pop":
        stack.pop()
    elif input_strings[0] == "size":
        stack.size()
    elif input_strings[0] == "empty":
        stack.empty()
    elif input_strings[0] == "top":
        stack.top()
