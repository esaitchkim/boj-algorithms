"""9237.py
Title: Planting Trees
Url: https://www.acmicpc.net/problem/9237
"""

N = int(input())
t = [*map(int, input().split())]
t.sort(reverse=True)
day = 1

for i in range(len(t)):
    tmp_day = i + 2 + t[i]
    if tmp_day > day:
        day = tmp_day

print(day)
