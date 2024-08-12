"""15829.py
Title: Hashing
Url: https://www.acmicpc.net/problem/15829
"""

L = int(input())
input_string = input()

r, M = 31, 1234567891

x = ord("a") - 1
res = 0

for i in range(L):
    res += (ord(input_string[i]) - x) * r ** (i)

res %= M

print(res)
