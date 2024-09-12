"""21300.py
Title: Bottle Return
Url: https://www.acmicpc.net/problem/21300
"""

bottles = map(int, input().split())
DEPOSIT = 5
res = sum(bottles) * DEPOSIT
print(res)
