"""29863.py
Title: Arno's Sleep Schedule
Url: https://www.acmicpc.net/problem/29863
"""

to_sleep = int(input())
wake_up = int(input())
sleep_time = 0
if 20 <= to_sleep <= 23:
    sleep_time = wake_up - to_sleep + 24
else:
    sleep_time = wake_up - to_sleep
print(sleep_time)
