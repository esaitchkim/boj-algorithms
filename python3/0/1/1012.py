"""1012.py
Title: 유기농 배추
Url: https://www.acmicpc.net/problem/1012
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for _ in range(T):
    cbg_dict = {}
    M, N, K = map(int, input().split())
    for _ in range(K):
        X, Y = map(int, input().split())
        cbg_dict[(X, Y)] = True

    earthwarm = 0
    while len(cbg_dict) > 0:
        earthwarm += 1
        cbg = list(cbg_dict.keys())[0]
        stack = [cbg]
        del cbg_dict[cbg]
        while len(stack) > 0:
            cbg = stack.pop()
            if cbg[0] - 1 >= 0:
                l_cbg = (cbg[0] - 1, cbg[1])
                if cbg_dict.get(l_cbg) is not None:
                    stack.append(l_cbg)
                    del cbg_dict[l_cbg]
            if cbg[0] + 1 < M:
                r_cbg = (cbg[0] + 1, cbg[1])
                if cbg_dict.get(r_cbg) is not None:
                    stack.append(r_cbg)
                    del cbg_dict[r_cbg]
            if cbg[1] - 1 >= 0:
                d_cbg = (cbg[0], cbg[1] - 1)
                if cbg_dict.get(d_cbg) is not None:
                    stack.append(d_cbg)
                    del cbg_dict[d_cbg]
            if cbg[1] + 1 < N:
                u_cbg = (cbg[0], cbg[1] + 1)
                if cbg_dict.get(u_cbg) is not None:
                    stack.append(u_cbg)
                    del cbg_dict[u_cbg]
    print(f"{earthwarm}\n")
