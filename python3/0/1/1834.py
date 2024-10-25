"""1834.py
Title: 나머지와 몫이 같은 수
Url: https://www.acmicpc.net/problem/1834
"""

N = int(input())
res = (N * (N - 1) // 2) * (N + 1)

print(res)
