"""1436.py
Title: 영화감독 숌
Url: https://www.acmicpc.net/problem/1436
"""

N = int(input())
cnt = 0
left_digits = 0
num = "666"
while True:
    cnt += 1
    num = str(left_digits) + "666"
    idx = num.find("6666")
    if idx >= 0:
        idx += 3
        num_length = len(num)
        right_length = num_length - idx
        max_increase_cnt = 10**right_length - 1
        if max_increase_cnt + cnt >= N:
            num = num[:idx] + str(N - cnt).rjust(right_length, "0")
            break
        else:
            cnt += max_increase_cnt
    if cnt == N:
        break
    left_digits += 1
num = int(num)
print(num)
