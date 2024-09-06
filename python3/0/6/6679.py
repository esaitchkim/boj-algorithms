"""6679.py
Title: Specialized Four-Digit Numbers
Url: https://www.acmicpc.net/problem/6679
"""

import sys

print = sys.stdout.write


def sum_digits(num, base):
    res = 0
    while num > 0:
        res += num % base
        num //= base
    return res


for num in range(1000, 10000):
    if sum_digits(num, 10) == sum_digits(num, 12) == sum_digits(num, 16):
        print(f"{num}\n")
