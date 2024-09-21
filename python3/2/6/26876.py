"""26876.py
Title: New Time
Url: https://www.acmicpc.net/problem/26876
"""

hh, mm = map(int, input().split(":"))
goal_hh, goal_mm = map(int, input().split(":"))

btn = 0

if mm > goal_mm:
    btn += goal_mm + 60 - mm
    hh += 1
else:
    btn += goal_mm - mm

if hh > goal_hh:
    btn += goal_hh + 24 - hh
else:
    btn += goal_hh - hh

print(btn)
