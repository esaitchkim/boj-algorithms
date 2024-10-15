"""2428.py
Title: Plagiarism
Url: https://www.acmicpc.net/problem/2428
"""

N = int(input())

F = [*map(int, input().split())]
F.sort()
res = 0

for i in range(len(F)):
    start = i + 1
    end = len(F) - 1

    while start <= end:
        mid = (start + end) // 2
        if F[i] >= F[mid] * 0.9:
            start = mid + 1
        else:
            end = mid - 1
    res += end - i

print(res)
