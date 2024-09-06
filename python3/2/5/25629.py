"""25629.py
Title: 홀짝 수열
Url: https://www.acmicpc.net/problem/25629
"""

N = int(input())
a = map(int, input().split())
flag = True

odd = []
even = []

for num in a:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if N // 2 != len(even):
    flag = False

if (N + 1) // 2 != len(odd):
    flag = False

if flag:
    print(1)
else:
    print(0)
