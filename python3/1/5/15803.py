"""15803.py
Title: PLAYERJINAH’S BOTTLEGROUNDS
Url: https://www.acmicpc.net/problem/15803
"""

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

#  CCW
if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")
