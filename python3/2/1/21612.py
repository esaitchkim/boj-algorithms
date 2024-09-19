"""21612.py
Title: Boiling Water
Url: https://www.acmicpc.net/problem/21612
"""

B = int(input())

P = 5 * B - 400

print(P)
if P < 100:
    print(1)
elif P == 100:
    print(0)
else:
    print(-1)
