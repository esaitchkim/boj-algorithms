"""21965.py
Title: 드높은 남산 위에 우뚝 선
Url: https://www.acmicpc.net/problem/21965
"""

N = int(input())
A = [*map(int, input().split())]

is_mountain = True
peak = False

for i in range(len(A) - 1):
    if peak:
        if A[i] <= A[i + 1]:
            is_mountain = False
            break
    if not peak:
        if A[i] > A[i + 1]:
            peak = True
        elif A[i] == A[i + 1]:
            is_mountain = False
            break

if is_mountain:
    print("YES")
else:
    print("NO")
