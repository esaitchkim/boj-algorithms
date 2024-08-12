"""10807.py
Title: 개수 세기
Url: https://www.acmicpc.net/problem/10807
"""

N = int(input())
num_list = [*map(int, input().split())]
v = int(input())

cnt_v = num_list.count(v)

print(cnt_v)
