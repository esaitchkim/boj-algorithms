"""10866.py
Title: 덱
Url: https://www.acmicpc.net/problem/10866
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push_front(self, x):
        if self._size == 0:
            self._front = self._back = Node(x)
        else:
            node = Node(x)
            node.next = self._front
            self._front.prev = node
            self._front = node
        self._size += 1

    def push_back(self, x):
        if self._size == 0:
            self._front = self._back = Node(x)
        else:
            node = Node(x)
            node.prev = self._back
            self._back.next = node
            self._back = node
        self._size += 1

    def pop_front(self):
        if self._size == 0:
            print("-1\n")
        else:
            node = self._front
            self._front = self._front.next
            print(f"{node.value}\n")
            self._size -= 1

    def pop_back(self):
        if self._size == 0:
            print("-1\n")
        else:
            node = self._back
            self._back = self._back.prev
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
deque = Deque()

for _ in range(N):
    input_strings = input().split()
    if input_strings[0] == "push_front":
        deque.push_front(int(input_strings[1]))
    elif input_strings[0] == "push_back":
        deque.push_back(int(input_strings[1]))
    elif input_strings[0] == "pop_front":
        deque.pop_front()
    elif input_strings[0] == "pop_back":
        deque.pop_back()
    elif input_strings[0] == "size":
        deque.size()
    elif input_strings[0] == "empty":
        deque.empty()
    elif input_strings[0] == "front":
        deque.front()
    elif input_strings[0] == "back":
        deque.back()
