"""11047.py
Title: 동전 0
Url: https://www.acmicpc.net/problem/11047
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coin_cnt = 0
for coin in coins[::-1]:
    cnt = K // coin
    coin_cnt += cnt
    K -= cnt * coin
    if K == 0:
        break

print(coin_cnt)
