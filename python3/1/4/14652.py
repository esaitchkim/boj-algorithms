"""14652.py
Title: 나는 행복합니다~
Url: https://www.acmicpc.net/problem/14652
"""

N, M, K = map(int, input().split())

m = K % M
n = K // M

print(f"{n} {m}")
