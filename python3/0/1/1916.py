"""1916.py
Title: 최소비용 구하기
Url: https://www.acmicpc.net/problem/1916
"""

import sys

input = sys.stdin.readline
INF = int(1e9)


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


class Deque:
    def __init__(self) -> None:
        self.__front = None
        self.__rear = None
        self.__size = 0

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
            return None

        value = self.__front.get_value()
        self.__front = self.__front.get_next()
        self.__size -= 1

        return value

    def is_empty(self):
        return True if self.__size == 0 else False

    def get_size(self):
        return self.__size


N = int(input())
M = int(input())

bus = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    A, B, cost = map(int, input().split())
    if bus[A][B] > cost:
        bus[A][B] = cost

A, B = map(int, input().split())

res = bus[A]
deque = Deque()
deque.enqueue([i for i in range(len(res)) if res[i] != INF])

while deque.is_empty() != True:
    a = deque.dequeue()
    for num in a:
        n_queue = []
        for i in range(1, N + 1):
            if res[i] > res[num] + bus[num][i]:
                res[i] = res[num] + bus[num][i]
                n_queue.append(i)
        if len(n_queue) > 0:
            deque.enqueue(n_queue)

print(res[B])
