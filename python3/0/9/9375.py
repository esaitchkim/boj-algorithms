"""9375.py
Title: Incognito
Url: https://www.acmicpc.net/problem/9375
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    attributes = {}
    n = int(input())
    for _ in range(n):
        name, category = input().rstrip().split()
        if attributes.get(category) is None:
            attributes[category] = 1
        else:
            attributes[category] += 1
    disguises = 1
    for v in attributes.values():
        disguises *= v + 1
    disguises -= 1
    print(f"{disguises}\n")
