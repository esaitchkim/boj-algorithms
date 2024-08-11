"""2753.py
Title: 윤년
Url: https://www.acmicpc.net/problem/2753
"""

year = int(input())
result = 0

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    result = 1

print(result)
