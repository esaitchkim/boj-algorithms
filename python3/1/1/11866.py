"""11866.py
Title: 요세푸스 문제 0
Url: https://www.acmicpc.net/problem/11866
"""


class Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def get_value(self):
        return self.__value

    def set_next(self, next):
        self.__next = next

    def set_value(self, value):
        self.__value = value


class Queue:
    def __init__(self) -> None:
        self.__front = None
        self.__back = None
        self.__size = 0

    def push(self, x):
        if self.__size == 0:
            self.__front = self.__back = Node(x)
        else:
            node = Node(x)
            self.__back.set_next(node)
            self.__back = node

        self.__size += 1

    def pop(self):
        if self.__size > 0:
            node = self.__front
            self.__front = node.get_next()
            self.__size -= 1
            return node.get_value()
        return None

    def skip(self):
        if self.__size > 0:
            value = self.pop()
            self.push(value)

    def get_size(self):
        return self.__size


N, K = map(int, input().split())
queue = Queue()
result_list = []
for i in range(1, N + 1):
    queue.push(i)

while queue.get_size() > 0:
    if queue.get_size() == 1:
        result_list.append(queue.pop())
        break
    for i in range(1, K):
        queue.skip()
    result_list.append(queue.pop())

print("<", end="")
print(*result_list, sep=", ", end="")
print(">")
