"""1546.py
Title: 평균
Url: https://www.acmicpc.net/problem/1546
"""

N = int(input())

grades = [*map(int, input().split())]
M = max(grades)
grades = [(i / M) * 100 for i in grades]

new_avg = sum(grades) / N

print(new_avg)
