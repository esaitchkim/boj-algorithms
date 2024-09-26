"""16431.py
Title: 베시와 데이지
Url: https://www.acmicpc.net/problem/16431
"""

Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())

bessie = 0
daisy = 0

bessie = abs(Br - Jr) + abs(Bc - Jc) - min(abs(Br - Jr), abs(Bc - Jc))
daisy = abs(Dr - Jr) + abs(Dc - Jc)

if bessie < daisy:
    print("bessie")
elif bessie > daisy:
    print("daisy")
else:
    print("tie")
