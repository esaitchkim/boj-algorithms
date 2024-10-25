"""2811.py
Title: ZIMA
Url: https://www.acmicpc.net/problem/2811
"""

N = int(input())

# 온도
winter_period = [*map(int, input().split())]

# 기간
period_list = []
# 최대 기간 목록
max_period_list = []
# 말할 수 있는 기간
announced_list = [0 for _ in range(N)]
# 최대 기간
max_period = 0
# 현 기간
period = 0

for i in range(N):
    if winter_period[i] < 0:
        period += 1
    else:
        if period != 0:
            if period > max_period:
                max_period_list = [i - period]
                max_period = period
            elif period == max_period:
                max_period_list.append(i - period)
            period_list.append([i - period, period])
            period = 0

if period != 0:
    if period > max_period:
        max_period_list = [N - period]
        max_period = period
    elif period == max_period:
        max_period_list.append(N - period)
    period_list.append([N - period, period])

for p in period_list:
    start = max(0, p[0] - p[1] * 2)
    end = p[0]
    for i in range(start, end):
        announced_list[i] = 1

t3_announced = 0

for p in max_period_list:
    start = max(0, p - max_period * 3)
    end = p
    temp_announced = announced_list[start:end].count(0)
    t3_announced = temp_announced if temp_announced > t3_announced else t3_announced

res = sum(announced_list) + t3_announced
print(res)
