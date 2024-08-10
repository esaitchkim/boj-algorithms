"""10809.py
Title: 알파벳 찾기
Url: https://www.acmicpc.net/problem/10809
"""

S = input()

alphabet_position = {chr(i): -1 for i in range(ord("a"), ord("z") + 1)}

for idx in range(len(S)):
    if alphabet_position[S[idx]] == -1:
        alphabet_position[S[idx]] = idx

alphabet_list = [alphabet_position[chr(i)] for i in range(ord("a"), ord("z") + 1)]
print(*alphabet_list, sep=" ")
