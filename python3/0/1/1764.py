"""1764.py
Title: 듣보잡
Url: https://www.acmicpc.net/problem/1764
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

p_dict = {}
result = []

for _ in range(N):
    never_heard = input().rstrip()
    p_dict[never_heard] = True

for _ in range(M):
    never_seen = input().rstrip()
    if p_dict.get(never_seen) is not None:
        result.append(never_seen)

result.sort()

print(f"{len(result)}\n")
for p in result:
    print(f"{p}\n")
