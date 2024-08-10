"""2675.py
Title: 문자열 반복
Url: https://www.acmicpc.net/problem/2675
"""

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    result_string = ""
    for s in S:
        result_string += (s) * R

    print(result_string)
