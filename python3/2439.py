"""2439.py
Title: 별 찍기 - 2
Url: https://www.acmicpc.net/problem/2438
"""

N = int(input())

print_string = '*'

for i in range(1,N+1):
    print((print_string*i).rjust(N))
