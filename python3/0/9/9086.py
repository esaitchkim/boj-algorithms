"""9086.py
Title: 문자열
Url: https://www.acmicpc.net/problem/9086
"""

T = int(input())
for _ in range(T):
    input_string = input()
    first_string, last_string = input_string[0], input_string[-1]
    print(f"{first_string}{last_string}")
