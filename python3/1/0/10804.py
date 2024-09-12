"""10804.py
Title: 카드 역배치
Url: https://www.acmicpc.net/problem/10804
"""

cards = [i for i in range(21)]

for _ in range(10):
    start, end = map(int, input().split())
    cards = cards[:start] + cards[end : start - 1 : -1] + cards[end + 1 :]

print(*cards[1:], sep=" ")
