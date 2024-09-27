"""1817.py
Title: 짐 챙기는 숌
Url: https://www.acmicpc.net/problem/1817
"""

N, M = map(int, input().split())
books = []
box = 0
box_weight = 0

if N > 0:
    books = [*map(int, input().split())]
    box = 1

for weight in books:
    if box_weight + weight > M:
        box += 1
        box_weight = weight
    else:
        box_weight += weight

print(box)
