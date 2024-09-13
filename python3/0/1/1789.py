"""1789.py
Title: 수들의 합
Url: https://www.acmicpc.net/problem/1789
"""

S = int(input())
tot = 1
i = 2
while True:
    tot += i
    if S < tot:
        break
    elif S == tot:
        i += 1
        break
    i += 1

print(i - 1)
