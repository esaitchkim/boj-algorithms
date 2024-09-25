"""5565.py
Title: レシート
Url: https://www.acmicpc.net/problem/5565
"""

total_price = int(input())
for _ in range(9):
    total_price -= int(input())

print(total_price)
