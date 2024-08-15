"""28113.py
Title: 정보섬의 대중교통
Url: https://www.acmicpc.net/problem/28113
"""

N, A, B = map(int, input().split())

bus = max(N, A)
subway = max(N, B)

result = "Anything"

if bus > subway:
    result = "Subway"
elif subway > bus:
    result = "Bus"

print(result)
