"""26550.py
Title: Ornaments
Url: https://www.acmicpc.net/problem/26550
"""

n = int(input())

for _ in range(n):
    layer = int(input())
    res = layer * (layer + 1) * (layer + 2) // 6
    print(res)