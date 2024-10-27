"""24993.py
Title: KIARA is a Recursive Acronym
Url: https://www.acmicpc.net/problem/24993
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

first_letters = {chr(c): False for c in range(ord("A"), ord("Z") + 1)}
word_list = []
is_exists = False

for _ in range(N):
    word = input().rstrip()
    first_letters[word[0]] = True
    word_list.append(word)


for word in word_list:
    flag = True
    for w in word:
        if not first_letters[w]:
            flag = False
            break
    if flag:
        is_exists = True
        break

print("Y\n" if is_exists else "N\n")
