"""10162.py
Title: 전자레인지
Url: https://www.acmicpc.net/problem/10162
"""

A = 5 * 60
B = 1 * 60
C = 10

cnt_A = 0
cnt_B = 0
cnt_C = 0

T = int(input())

if T % C != 0:
    print(-1)
else:
    cnt_A += T // A
    T %= A
    cnt_B += T // B
    T %= B
    cnt_C += T // C
    print(cnt_A, cnt_B, cnt_C, sep=" ")
