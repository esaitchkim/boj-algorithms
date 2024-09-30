"""10815.py
Title: 숫자 카드
Url: https://www.acmicpc.net/problem/10815
"""

N = int(input())
cards = {i: True for i in map(int, input().split())}

M = int(input())
question = map(int, input().split())

for card in question:
    if cards.get(card):
        print("1", end=" ")
    else:
        print("0", end=" ")
