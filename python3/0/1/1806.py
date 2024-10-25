"""1806.py
Title: Subsequence
Url: https://www.acmicpc.net/problem/1806
"""

N, S = map(int, input().split())

sequence = [*map(int, input().split())]
seq_len = N + 1

start, end = 0, 0
seq_sum = sequence[0]

while start <= end:
    if seq_sum >= S:
        if seq_len >= end - start + 1:
            seq_len = end - start + 1
        seq_sum -= sequence[start]
        start += 1
    else:
        if end < N - 1:
            end += 1
            seq_sum += sequence[end]
        else:
            break

if seq_len == N + 1:
    seq_len = 0
print(seq_len)
