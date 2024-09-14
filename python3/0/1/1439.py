"""1439.py
Title: 뒤집기
Url: https://www.acmicpc.net/problem/1439
"""

S = input()

cnt_dict = {"0": 0, "1": 0}
before_char = S[0]

for char in S[1:]:
    if char != before_char:
        cnt_dict[before_char] += 1
        before_char = char
cnt_dict[char] += 1

print(min(cnt_dict.values()))
