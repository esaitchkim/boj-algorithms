"""15904.py
Title: UCPC는 무엇의 약자일까?
Url: https://www.acmicpc.net/problem/15904
"""

input_string = input()

answer = "UCPC"
word = ""

for c in input_string:
    if len(word) == 4:
        break

    if c == answer[len(word)]:
        word += c

if word == answer:
    print("I love UCPC")
else:
    print("I hate UCPC")
