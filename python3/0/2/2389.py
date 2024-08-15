"""2389.py
Title: ŠEĆER
Url: https://www.acmicpc.net/problem/2389
"""

N = int(input())

packages = 0
imp_list = [4, 7]

result = -1

if N not in imp_list:
    packages = N // 5
    N -= 5 * packages

    if N == 0:
        result = packages
    elif N == 1:
        result = packages + 1
    elif N == 2:
        result = packages + 2
    elif N == 3:
        result = packages + 1
    else:
        result = packages + 2

print(result)
