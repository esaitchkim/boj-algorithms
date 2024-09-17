"""18221.py
Title: 교수님 저는 취업할래요
Url: https://www.acmicpc.net/problem/18221
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

classroom = []

prof = [0, 0]
sk = [0, 0]

flag_5 = True
flag_2 = True

for i in range(N):
    line = [*map(int, input().split())]
    classroom.append(line)
    if flag_2 and 2 in line:
        sk = [i, line.index(2)]
        flag_2 = False
    if flag_5 and 5 in line:
        prof = [i, line.index(5)]
        flag_5 = False

dist = (prof[0] - sk[0]) ** 2 + (prof[1] - sk[1]) ** 2

if dist < 25:
    print("0\n")
else:
    cnt = 0
    for x in range(min(prof[0], sk[0]), max(prof[0], sk[0]) + 1):
        for y in range(min(prof[1], sk[1]), max(prof[1], sk[1]) + 1):
            if classroom[x][y] == 1:
                cnt += 1
    if cnt >= 3:
        print("1\n")
    else:
        print("0\n")
