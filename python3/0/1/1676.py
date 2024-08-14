"""1676.py
Title: 팩토리얼 0의 개수
Url: https://www.acmicpc.net/problem/1676
"""

N = int(input())

cnt_2 = 0
cnt_5 = 0

for i in range(N, 0, -1):
    while i % 2 == 0:
        i //= 2
        cnt_2 += 1
    while i % 5 == 0:
        i //= 5
        cnt_5 += 1

res = min(cnt_2, cnt_5)
print(res)
