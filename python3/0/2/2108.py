"""2108.py
Title: 통계학
Url: https://www.acmicpc.net/problem/2108
"""

import sys

input = sys.stdin.readline

N = int(input())
num_dict = {}

for _ in range(N):
    num = int(input())
    if num_dict.get(num) is None:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

num_list = sorted(num_dict.keys())
sum_nums = 0
median_cnt = (N // 2) + 1
median = None
cnt = 0
most_numbers = []
mode_cnt = 0
diff = num_list[-1] - num_list[0]

for num in num_list:
    sum_nums += num * num_dict[num]
    if cnt < median_cnt:
        cnt += num_dict[num]
        if cnt >= median_cnt:
            median = num

    if num_dict[num] > mode_cnt:
        most_numbers = [num]
        mode_cnt = num_dict[num]
    elif num_dict[num] == mode_cnt:
        most_numbers.append(num)

print(round(sum_nums / N))
print(median)
print(most_numbers[0] if len(most_numbers) == 1 else most_numbers[1])
print(diff)
