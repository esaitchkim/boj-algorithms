"""16953.py
Title: A → B
Url: https://www.acmicpc.net/problem/16953
"""


class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def get_value(self):
        return self.__value

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next


class Queue:
    def __init__(self):
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
            return None
        else:
            value = self.__front.get_value()
            self.__front = self.__front.get_next()
            self.__size -= 1
            return value


A, B = map(int, input().split())
res = -1

que = Queue()
que.enqueue([A])
cnt = 0
while que.get_size() > 0:
    cnt += 1
    node_list = que.dequeue()
    next_list = []
    for num in node_list:
        if num == B:
            res = cnt
            break
        else:
            next_num_1 = num * 2
            next_num_2 = num * 10 + 1
            if next_num_1 <= B:
                next_list.append(next_num_1)
            if next_num_2 <= B:
                next_list.append(next_num_2)
    if len(next_list):
        que.enqueue(next_list)

print(res)
