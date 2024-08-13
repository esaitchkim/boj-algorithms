"""10989.py
Title: 수 정렬하기 3
Url: https://www.acmicpc.net/problem/10989
"""

# case 1
# import sys

# input = sys.stdin.readline
# print = sys.stdout.write

# N = int(input())

# number_list = [0 for _ in range(10001)]
# total_cnt = 0
# cnt = 0
# for _ in range(N):
#     number = int(input())
#     number_list[number] += 1

# for i in range(10001):
#     if number_list[i] > 0:
#         for j in range(number_list[i]):
#             print(f"{i}\n")

# case 2
# 속도 조금 개선
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

number_list = [0 for _ in range(10001)]
total_cnt = 0
cnt = 0
for _ in range(N):
    number = int(input())
    number_list[number] += 1

for i in range(10001):
    if number_list[i] > 0:
        while number_list[i] > 0:
            cnt = min(100000, number_list[i])
            number_list[i] -= cnt
            total_cnt += cnt
            print(f"{i}\n" * cnt)

    if total_cnt == N:
        break
