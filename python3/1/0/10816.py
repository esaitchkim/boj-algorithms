"""10816.py
Title: 숫자 카드 2
Url: https://www.acmicpc.net/problem/10816
"""

N = int(input())
card_dict = {}
for card in map(int, input().split()):
    if card_dict.get(card) is None:
        card_dict[card] = 1
    else:
        card_dict[card] += 1

M = int(input())

card_cnts = [
    0 if card_dict.get(card) is None else card_dict.get(card)
    for card in map(int, input().split())
]

print(*card_cnts, sep=" ")
