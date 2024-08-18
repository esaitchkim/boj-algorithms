"""17219.py
Title: 비밀번호 찾기
Url: https://www.acmicpc.net/problem/17219
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

passwords = {}

for _ in range(N):
    site, pw = input().rstrip().split(" ")
    passwords[site] = pw

for _ in range(M):
    site = input().rstrip()
    pw = passwords[site]
    print(f"{pw}\n")
