"""13549.py
Title: 숨바꼭질 3
Url: https://www.acmicpc.net/problem/13549
"""


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


class Dequeue:
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
            return None
        value = self.__front.get_value()
        self.__front = self.__front.get_next()
        self.__size -= 1
        return value


N, K = map(int, input().split())
visited = [False] * 200001

sec = 0
queue = Dequeue()
queue.enqueue([N])
visited[N] = True

while queue.get_size() > 0:
    flag = False
    nodes = queue.dequeue()
    i = 0
    while i < len(nodes):
        if nodes[i] == K or nodes[i] * 2 == K:
            flag = True
            break
        if nodes[i] < K and visited[nodes[i] * 2] == False:
            visited[nodes[i] * 2] = True
            nodes.append(nodes[i] * 2)
        i += 1

    if flag:
        break

    nexts = []
    for num in nodes:
        if visited[num - 1] == False and num > 0:
            visited[num - 1] = True
            nexts.append(num - 1)
        if visited[num + 1] == False and num < 200000:
            visited[num + 1] = True
            nexts.append(num + 1)

    queue.enqueue(nexts)
    sec += 1

print(sec)
