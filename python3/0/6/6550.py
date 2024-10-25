"""6550.py
Title: All in All
Url: https://www.acmicpc.net/problem/6550
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

while True:
    try:
        s, t = input().rstrip().split()
    except Exception as e:
        break

    idx = 0
    for c in t:
        if c == s[idx]:
            idx += 1
        if len(s) == idx:
            break
    if len(s) == idx:
        print("Yes\n")
    else:
        print("No\n")
