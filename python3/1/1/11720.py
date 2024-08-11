"""11720.py
Title: 숫자의 합
Url: https://www.acmicpc.net/problem/11720
"""

N = int(input())
num_string = input()
result = 0
for num in num_string:
    result += int(num)

print(result)
