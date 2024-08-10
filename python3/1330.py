"""1330.py
Title: 두 수 비교하기
Url: https://www.acmicpc.net/problem/1330
"""

A, B = map(int, input().split())

result = None

if A > B:
    result = ">"
elif A < B:
    result = "<"
else:
    result = "=="


print(result)
