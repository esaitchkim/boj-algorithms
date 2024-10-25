"""1076.py
Title: 저항
Url: https://www.acmicpc.net/problem/1076
"""

resistance = {
    "black": [0, 1],
    "brown": [1, 10],
    "red": [2, 100],
    "orange": [3, 1000],
    "yellow": [4, 10000],
    "green": [5, 100000],
    "blue": [6, 1000000],
    "violet": [7, 10000000],
    "grey": [8, 100000000],
    "white": [9, 1000000000],
}

re1 = resistance[input()][0] * 10
re2 = resistance[input()][0]
re3 = resistance[input()][1]

res = (re1 + re2) * re3
print(res)
