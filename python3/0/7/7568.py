"""7568.py
Title: 덩치
Url: https://www.acmicpc.net/problem/7568
"""

N = int(input())

p_list = []
orders = [N for _ in range(N)]

for _ in range(N):
    x, y = map(int, input().split())
    p_list.append((x, y))

for i in range(N):
    for j in range(N):
        if i != j and (p_list[i][0] >= p_list[j][0] or p_list[i][1] >= p_list[j][1]):
            orders[i] -= 1

print(*orders, sep=" ")
