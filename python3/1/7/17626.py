"""17626.py
Title: Four Squares
Url: https://www.acmicpc.net/problem/17626
"""

n = int(input())

min_number = 4

num_1 = int(n**0.5)
for num1 in range(int(n**0.5), int((n**0.5) // 3), -1):
    tmp_num1 = n - (num1**2)
    if tmp_num1 == 0:
        min_number = 1
        break

    for num2 in range(int(tmp_num1**0.5), int((tmp_num1**0.5) // 2), -1):
        tmp_num2 = tmp_num1 - (num2**2)
        tmp_num3 = int(tmp_num2**0.5)
        if tmp_num2 == 0:
            min_number = min(min_number, 2)
        elif tmp_num3**2 == tmp_num2:
            min_number = min(min_number, 3)
            break

    if min_number <= 2:
        break

print(min_number)
