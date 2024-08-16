"""9012.py
Title: Parenthesis
Url: https://www.acmicpc.net/problem/9012
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    input_ps = input().rstrip()
    ps_length = len(input_ps)
    while ps_length > 0:
        input_ps = input_ps.replace("()", "")
        after_length = len(input_ps)
        if ps_length == after_length:
            break

        ps_length = after_length

    if len(input_ps) == 0:
        print("YES\n")
    else:
        print("NO\n")
