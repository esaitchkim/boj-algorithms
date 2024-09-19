"""14924.py
Title: 폰 노이만과 파리
Url: https://www.acmicpc.net/problem/14924
"""

S, T, D = map(int, input().split())

hour = D // (S * 2)
F = T * hour
print(F)
