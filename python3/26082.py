"""26082.py
Title: WARBOY
Url: https://www.acmicpc.net/problem/26082
"""

A, B, C = map(int, input().split())

cost_effectiveness = (B // A) * 3
performance = cost_effectiveness * C

print(performance)
