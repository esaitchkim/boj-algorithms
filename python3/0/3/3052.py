"""3052.py
Title: 나머지
Url: https://www.acmicpc.net/problem/3052
"""

mod_set = set()

for i in range(10):
    number = int(input())
    mod = number % 42
    mod_set.add(mod)

result = len(mod_set)

print(result)
