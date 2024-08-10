"""2562.py
Title: 최댓값
Url: https://www.acmicpc.net/problem/2562
"""

max_number = 0
number_index = 0
for i in range(1,10):
    input_number = int(input())
    if input_number > max_number:
        max_number = input_number
        number_index = i

print(max_number)
print(number_index)
