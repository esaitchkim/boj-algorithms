"""1620.py
Title: 나는야 포켓몬 마스터 이다솜
Url: https://www.acmicpc.net/problem/1620
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
pokedex = {}

for i in range(1, N + 1):
    pokemon = input().rstrip()
    pokedex[pokemon] = i
    pokedex[str(i)] = pokemon

for _ in range(M):
    input_string = input().rstrip()
    print(f"{pokedex[input_string]}\n")
