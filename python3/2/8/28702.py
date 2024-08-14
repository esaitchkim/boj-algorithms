"""28702.py
Title: FizzBuzz
Url: https://www.acmicpc.net/problem/28702
"""

input1 = input()
input2 = input()
input3 = input()

next_num = 0
res = ""
if input1.isnumeric():
    next_num = int(input1) + 3
elif input2.isnumeric():
    next_num = int(input2) + 2
elif input3.isnumeric():
    next_num = int(input3) + 1

if next_num % 3 == 0:
    res += "Fizz"

if next_num % 5 == 0:
    res += "Buzz"

if res == "":
    res = next_num

print(res)
