"""25400.py
Title: 제자리
Url: https://www.acmicpc.net/problem/25400
"""

N = int(input())
A = [*map(int, input().split())]

cnt = 0
now_num = 1

for num in A:
    if num == now_num:
        now_num += 1
    else:
        cnt += 1

print(cnt)
