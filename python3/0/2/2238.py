"""2238.py
Title: 경매
Url: https://www.acmicpc.net/problem/2238
"""

U, N = map(int, input().split())
price_dict = {}

for _ in range(N):
    S, P = input().split()
    P = int(P)
    if price_dict.get(P) is None:
        price_dict[P] = [S]
    else:
        price_dict[P].append(S)

res = sorted(price_dict.items(), key=lambda x: (len(x[1]), x[0]))[0]

print(res[1][0], res[0])
