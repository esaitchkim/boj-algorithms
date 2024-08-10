"""2475.py
Title: 검증수
Url: https://www.acmicpc.net/problem/2475
"""

serials = list(map(int, input().split()))

valid_number = sum([i**2 for i in serials])%10

print(valid_number)
