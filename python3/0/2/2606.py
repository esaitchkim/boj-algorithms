"""2606.py
Title: 바이러스
Url: https://www.acmicpc.net/problem/2606
"""

import sys

input = sys.stdin.readline

n = int(input())
nodes = int(input())
graph = {i: set() for i in range(1, n + 1)}

for _ in range(nodes):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = []
stack = [1]

while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        stack += graph[node] - set(visited)

infected = len(visited) - 1

print(infected)
