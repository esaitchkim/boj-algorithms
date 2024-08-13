"""2775.py
Title: 부녀회장이 될테야
Url: https://www.acmicpc.net/problem/2775
"""

apartment = [[1 for _ in range(14)] for _ in range(15)]
apartment[0] = [i for i in range(1, 15)]
for i in range(1, 15):
    for j in range(1, 14):
        apartment[i][j] = apartment[i - 1][j] + apartment[i][j - 1]


T = int(input())


for _ in range(T):
    k = int(input())
    n = int(input())
    print(apartment[k][n - 1])
