"""9498.py
Title: 시험 성적
Url: https://www.acmicpc.net/problem/9498
"""

score = int(input())

result = "F"
if 90 <= score <= 100:
    result = "A"
elif 80 <= score <= 89:
    result = "B"
elif 70 <= score <= 79:
    result = "C"
elif 60 <= score <= 69:
    result = "D"

print(result)
