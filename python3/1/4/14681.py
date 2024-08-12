"""14681.py
Title: 사분면 고르기
Url: https://www.acmicpc.net/problem/14681
"""

x = int(input())
y = int(input())

quadrant = 0

if x > 0:
    quadrant = 1 if y > 0 else 4
else:
    quadrant = 2 if y > 0 else 3

print(quadrant)
