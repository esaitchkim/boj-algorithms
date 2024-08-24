"""11725.py
Title: 트리의 부모 찾기
Url: https://www.acmicpc.net/problem/11725
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write


class Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__next = None

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next


class Queue:
    def __init__(self) -> None:
        self.__front = None
        self.__rear = None
        self.__size = 0

    def get_size(self):
        return self.__size

    def enqueue(self, value):
        if self.__size == 0:
            self.__front = self.__rear = Node(value)
        else:
            node = Node(value)
            self.__rear.set_next(node)
            self.__rear = node
        self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            self.__front = self.__rear = None
            return None
        else:
            value = self.__front.get_value()
            self.__front = self.__front.get_next()
            self.__size -= 1
            return value


N = int(input())
tree = {}
for _ in range(N - 1):
    u, v = map(int, input().split())
    if tree.get(u) is None:
        tree[u] = [v]
    else:
        tree[u].append(v)

    if tree.get(v) is None:
        tree[v] = [u]
    else:
        tree[v].append(u)

queue = Queue()
queue.enqueue(1)
result = [0] * (N + 1)

while queue.get_size() > 0:
    node = queue.dequeue()
    for v in tree[node]:
        if result[v] == 0:
            result[v] = node
            queue.enqueue(v)

for element in result[2:]:
    print(f"{element}\n")
