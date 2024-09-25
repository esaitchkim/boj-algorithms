"""26307.py
Title: Correct
Url: https://www.acmicpc.net/problem/26307
"""

START_HOUR = 9
START_MINIUTE = 0

HH, MM = map(int, input().split())

elapsed_minute = (HH - START_HOUR) * 60 + (MM - START_MINIUTE)
print(elapsed_minute)
