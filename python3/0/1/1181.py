"""1181.py
Title: 단어 정렬
Url: https://www.acmicpc.net/problem/1181
"""

N = int(input())

word_dict = {i: set() for i in range(1, 51)}
for _ in range(N):
    input_string = input()
    input_lens = len(input_string)

    word_dict[input_lens].add(input_string)

for i in range(1, 51):
    if len(word_dict[i]) > 0:
        word_list = sorted(word_dict[i])
        print(*word_list, sep="\n")
