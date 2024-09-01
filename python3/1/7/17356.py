"""17356.py
Title: 욱 제
Url: https://www.acmicpc.net/problem/17356
"""

A, B = map(int, input().split())

M = (B - A) / 400
ratio = 1 / (1 + 10**M)
print(ratio)
