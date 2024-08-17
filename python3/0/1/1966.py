"""1966.py
Title: Printer Queue
Url: https://www.acmicpc.net/problem/1966
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

    def set_value(self, value):
        self.__value = value

    def set_next(self, next):
        self.__next = next


class PrinterQueue:
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
        else:
            value = self.__front.get_value()
            self.__front = self.__front.get_next()
            self.__size -= 1
            return value

    def get_size(self):
        return self.__size


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    printQueue = PrinterQueue()
    priorities = map(int, input().split())
    p_dict = {}
    for doc in priorities:
        if p_dict.get(doc) is None:
            p_dict[doc] = 1
        else:
            p_dict[doc] += 1
        printQueue.enqueue(doc)

    printCnt = 0
    while True:
        max_priorities = max(p_dict.keys())
        value = printQueue.dequeue()
        if value == max_priorities:
            printCnt += 1
            if M == 0:
                print(f"{printCnt}\n")
                break
            p_dict[value] -= 1
            if p_dict[value] == 0:
                del p_dict[value]
        else:
            printQueue.enqueue(value)

        if M == 0:
            M = printQueue.get_size() - 1
        else:
            M -= 1
