"""1978.py
Title: 소수 찾기
Url: https://www.acmicpc.net/problem/1978
"""

N = int(input())
numbers = map(int, input().split())

num_of_primes = 0
prime_list = [True for _ in range(1001)]
prime_list[0], prime_list[1] = False, False

i = 2
while i**2 <= 1000:
    if prime_list[i]:
        for j in range(i * i, 1001, i):
            prime_list[j] = False
    i += 1


for number in numbers:
    if prime_list[number]:
        num_of_primes += 1

print(num_of_primes)
