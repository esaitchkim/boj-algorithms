"""28097.py
Title: 모범생 포닉스
Url: https://www.acmicpc.net/problem/28097
"""

N = int(input())
Ts = [*map(int, input().split())]

hours = sum(Ts) + (len(Ts) - 1) * 8
days = hours // 24
hours %= 24

print(f"{days} {hours}")
