"""31450.py
Title: Everyone is a winner
Url: https://www.acmicpc.net/problem/31450
"""

M, K = map(int, input().split())

if M % K == 0:
    print("Yes")
else:
    print("No")
