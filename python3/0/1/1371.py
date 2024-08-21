"""1371.py
Title: 가장 많은 글자
Url: https://www.acmicpc.net/problem/1371
"""

alphabet_dict = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}
max_alphabet = []
max_cnt = 0
for _ in range(50):
    try:
        input_line = input()
        for char in input_line:
            if char != " ":
                cnt = alphabet_dict[char] + 1
                if cnt > max_cnt:
                    max_alphabet = [char]
                    max_cnt = cnt
                elif cnt == max_cnt:
                    max_alphabet.append(char)
                alphabet_dict[char] = cnt
    except Exception as e:
        break

print(*sorted(max_alphabet), sep="")
