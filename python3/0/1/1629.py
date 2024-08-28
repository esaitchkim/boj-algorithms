"""1629.py
Title: 곱셈
Url: https://www.acmicpc.net/problem/1629
"""

A, B, C = map(int, input().split())
mul_list = [0, A % C]

bin_B = [int(i) for i in reversed(format(B, "b").zfill(32) + "0")]
res = mul_list[1] if bin_B[1] == 1 else 1

for i in range(2, len(bin_B)):
    mul_list.append((mul_list[i - 1] * mul_list[i - 1]) % C)
    if bin_B[i] == 1:
        res = (res * mul_list[i]) % C

print(res)
