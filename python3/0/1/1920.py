"""1920.py
Title: 수 찾기
Url: https://www.acmicpc.net/problem/1920
"""

import sys

print = sys.stdout.write

N = int(input())
num_dict = {i: True for i in map(int, input().split())}

M = int(input())
find_numbers = map(int, input().split())

for num in find_numbers:
    if num_dict.get(num):
        print("1\n")
    else:
        print("0\n")
