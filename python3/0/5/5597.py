"""5597.py
Title: 과제 안 내신 분..?
Url: https://www.acmicpc.net/problem/5597
"""

students = {i: True for i in range(1, 31)}

for _ in range(28):
    n = int(input())
    del students[n]

students = sorted(list(students.keys()))
print(students[0])
print(students[1])
