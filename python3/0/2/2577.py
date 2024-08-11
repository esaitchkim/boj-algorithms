"""2577.py
Title: 숫자의 개수
Url: https://www.acmicpc.net/problem/2577
"""

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
number_dict = {i: 0 for i in range(10)}

for i in result:
    number_dict[int(i)] += 1

for i in range(10):
    print(number_dict[i])
