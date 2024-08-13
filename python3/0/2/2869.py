"""2869.py
Title: 달팽이는 올라가고 싶다
Url: https://www.acmicpc.net/problem/2869
"""

A, B, V = map(int, input().split())

climb = A - B
V -= A
day = 1

day += V // climb

if (climb * (day - 1)) != V:
    day += 1

print(day)
