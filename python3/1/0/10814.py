"""10814.py
Title: 나이순 정렬
Url: https://www.acmicpc.net/problem/10814
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
members = []

for i in range(N):
    age, name = input().rstrip().split()
    age = int(age)
    members.append((i, age, name))

members.sort(key=lambda x: (x[1], x[0]))

for member in members:
    print(f"{member[1]} {member[2]}\n")
