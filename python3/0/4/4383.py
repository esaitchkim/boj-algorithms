"""4383.py
Title: Jolly Jumpers
Url: https://www.acmicpc.net/problem/4383
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

while True:
    try:
        n, *seq = map(int, input().split())
        diff_set = set()
        if n == 1:
            print("Jolly\n")
        else:
            flag = True
            befor_num = seq[0]
            for num in seq[1:]:
                diff = abs(num - befor_num)
                befor_num = num
                before_len = len(diff_set)
                if 1 <= diff < n:
                    diff_set.add(diff)
                after_len = len(diff_set)
                if before_len == after_len:
                    flag = False
                    break
            if flag:
                print("Jolly\n")
            else:
                print("Not jolly\n")

    except Exception as e:
        break
