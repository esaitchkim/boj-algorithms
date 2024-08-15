"""4949.py
Title: The Balance of the World
Url: https://www.acmicpc.net/problem/4949
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

brackets = "()[]"

while True:
    input_string = input().rstrip()
    if input_string == ".":
        break
    result_string = ""
    for char in input_string:
        if char in brackets:
            result_string += char

    string_length = len(result_string)
    while len(result_string) > 0:
        result_string = result_string.replace("()", "")
        result_string = result_string.replace("[]", "")
        if len(result_string) == string_length:
            break
        string_length = len(result_string)

    if string_length == 0:
        print("yes\n")
    else:
        print("no\n")
