"""1541.py
Title: 잃어버린 괄호
Url: https://www.acmicpc.net/problem/1541
"""

input_string = input()

result = 0
minus = False
left_numbers = []
right_numbers = []
cur_number = ""
for char in input_string:
    if char.isdigit():
        cur_number += char
    else:
        if minus:
            right_numbers.append(int(cur_number))
        else:
            left_numbers.append(int(cur_number))
        cur_number = ""
        if char == "-":
            minus = True

if minus:
    right_numbers.append(int(cur_number))
else:
    left_numbers.append(int(cur_number))

l_sum = sum(left_numbers)
r_sum = sum(right_numbers)

print(l_sum - r_sum)
