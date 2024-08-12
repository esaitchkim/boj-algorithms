"""1259.py
Title: 팰린드롬수
Url: https://www.acmicpc.net/problem/1259
"""

while True:
    num = input()
    result_print = "yes"
    if num == "0":
        break
    for i in range(len(num) // 2):
        if num[i] != num[-(i + 1)]:
            result_print = "no"
            break
    print(result_print)
