"""10845.py
Title: 큐
Url: https://www.acmicpc.net/problem/10845
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push(self, x):
        if self._size == 0:
            self._front = self._back = Node(x)
        else:
            node = Node(x)
            self._back.next = node
            self._back = node
        self._size += 1

    def pop(self):
        if self._size == 0:
            print("-1\n")
        else:
            node = self._front
            self._front = self._front.next
            print(f"{node.value}\n")
            self._size -= 1

    def size(self):
        print(f"{self._size}\n")

    def empty(self):
        if self._size == 0:
            print("1\n")
        else:
            print("0\n")

    def front(self):
        if self._size == 0:
            print("-1\n")
        else:
            print(f"{self._front.value}\n")

    def back(self):
        if self._size == 0:
            print("-1\n")
        else:
            print(f"{self._back.value}\n")


N = int(input())
queue = Queue()

for _ in range(N):
    input_strings = input().split()

    if input_strings[0] == "push":
        queue.push(int(input_strings[1]))
    elif input_strings[0] == "pop":
        queue.pop()
    elif input_strings[0] == "size":
        queue.size()
    elif input_strings[0] == "empty":
        queue.empty()
    elif input_strings[0] == "front":
        queue.front()
    elif input_strings[0] == "back":
        queue.back()
