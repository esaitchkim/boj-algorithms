"""4766.py
Title: A Simple Question of Chemistry
Url: https://www.acmicpc.net/problem/4766
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

b_tpr = float(input())

while True:
    a_tpr = float(input())
    if a_tpr == 999:
        break
    diff_tpr = a_tpr - b_tpr
    b_tpr = a_tpr
    print(f"{diff_tpr:.2f}\n")
