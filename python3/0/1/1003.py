"""1003.py
Title: 피보나치 함수
Url: https://www.acmicpc.net/problem/1003
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

fibo_0 = [0] * 41
fibo_1 = [0] * 41
fibo_0[0] = 1
fibo_1[1] = 1

for i in range(2, 41):
    fibo_0[i] = fibo_0[i - 1] + fibo_0[i - 2]
    fibo_1[i] = fibo_1[i - 1] + fibo_1[i - 2]


T = int(input())

for _ in range(T):
    N = int(input())
    print(f"{fibo_0[N]} {fibo_1[N]}\n")
