"""17010.py
Title: Time to Decompress
Url: https://www.acmicpc.net/problem/17010
"""

L = int(input())

for _ in range(L):
    n, c = input().split()
    n = int(n)
    print(c * n)
