"""17087.py
Title: 숨바꼭질 6
Url: https://www.acmicpc.net/problem/17087
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N, S = map(int, input().split())
A = [abs(i - S) for i in map(int, input().split())]
A.sort()

if N == 1:
    D = A[0]
else:
    D = A[0]
    for num in A[1:]:
        D = gcd(D, num)

print(D)
