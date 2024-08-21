"""17094.py
Title: Serious Problem
Url: https://www.acmicpc.net/problem/17094
"""

N = int(input())
s = input()

count_2 = s.count("2")
count_e = N - count_2

if count_2 > count_e:
    print(2)
elif count_2 < count_e:
    print("e")
else:
    print("yee")
