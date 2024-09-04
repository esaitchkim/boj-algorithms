"""16693.py
Title: Pizza Deal
Url: https://www.acmicpc.net/problem/16693
"""

import math

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

a = A1 / P1
r = R1 * R1 * math.pi / P2

print("Whole pizza") if r > a else print("Slice of pizza")
