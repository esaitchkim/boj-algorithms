"""13305.py
Title: 주유소
Url: https://www.acmicpc.net/problem/13305
"""

N = int(input())

roads = [*map(int, input().split())]
prices = [*map(int, input().split())]

cost = 0
price = prices[0]

for i in range(len(roads)):
    cost += price * roads[i]
    price = min(price, prices[i + 1])

print(cost)
