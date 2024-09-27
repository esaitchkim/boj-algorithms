"""19843.py
Title: 수면 패턴
Url: https://www.acmicpc.net/problem/19843
"""

day_dict = {}
day_dict["Mon"] = 24 * 0
day_dict["Tue"] = 24 * 1
day_dict["Wed"] = 24 * 2
day_dict["Thu"] = 24 * 3
day_dict["Fri"] = 24 * 4

T, N = map(int, input().split())

for _ in range(N):
    D1, H1, D2, H2 = input().split()
    D1, D2 = day_dict.get(D1), day_dict.get(D2)
    H1, H2 = int(H1), int(H2)
    T -= (D2 + H2) - (D1 + H1)

if T > 48:
    print(-1)
else:
    print(max(T, 0))
