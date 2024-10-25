"""26267.py
Title: 은?행 털!자 1
Url: https://www.acmicpc.net/problem/26267
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

bank_dict = {}


for _ in range(N):
    xi, ti, ci = map(int, input().split())
    if bank_dict.get(xi - ti) is None:
        bank_dict[xi - ti] = ci
    else:
        bank_dict[xi - ti] += ci

print(f"{max(bank_dict.values())}\n")
