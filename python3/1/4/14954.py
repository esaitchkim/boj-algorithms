"""14954.py
Title: Happy Number
Url: https://www.acmicpc.net/problem/14954
"""

n = int(input())

cycle = set()
cycle.add(n)

before_len = 0
after_len = len(cycle)

while before_len != after_len:
    before_len = len(cycle)
    n = sum([int(i) ** 2 for i in str(n)])
    cycle.add(n)
    after_len = len(cycle)

if n == 1:
    print("HAPPY")
else:
    print("UNHAPPY")
