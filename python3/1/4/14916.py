"""14916.py
Title: 거스름돈
Url: https://www.acmicpc.net/problem/14916
"""

COIN_5 = 5
COIN_2 = 2

cnt_5 = 0
cnt_2 = 0

change = int(input())
min_coin = change // 2 + 1
flag = False

while True:
    if COIN_5 * cnt_5 > change:
        break
    calc_change = change - (COIN_5 * cnt_5)
    cnt_2 = calc_change // COIN_2
    calc_change %= COIN_2
    if calc_change == 0:
        total_coin = cnt_2 + cnt_5
        min_coin = min(min_coin, total_coin)
        flag = True
    cnt_5 += 1

if flag:
    print(min_coin)
else:
    print(-1)
