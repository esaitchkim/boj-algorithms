"""1260.py
Title: DFS와 BFS
Url: https://www.acmicpc.net/problem/1260
"""

import sys

input = sys.stdin.readline


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

    def push(self, value):
        if self.__size == 0:
            self.__front = self.__rear = Node(value)
        else:
            node = Node(value)
            self.__rear.set_next(node)
            self.__rear = node
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return None
        else:
            value = self.__front.get_value()
            self.__front = self.__front.get_next()
            self.__size -= 1
            return value

    def get_size(self):
        return self.__size


N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (N + 1)
visited[0] = True
stack = [V]
result = []
while stack:
    node = stack.pop()
    if visited[node] == False:
        visited[node] = True
        result.append(node)
        stack.extend(sorted(graph[node], reverse=True))

print(*result, sep=" ")


visited = [False] * (N + 1)
visited[0] = True

queue = Queue()
queue.push(V)
result = []
while queue.get_size() > 0:
    node = queue.pop()
    if visited[node] == False:
        result.append(node)
        visited[node] = True
        for v in sorted(graph[node]):
            if visited[v] == False:
                queue.push(v)

print(*result, sep=" ")
