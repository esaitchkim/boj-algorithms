"""2609.py
Title: 최대공약수와 최소공배수
Url: https://www.acmicpc.net/problem/2609
"""


def gcd(a: int, b: int):
    """최대공약수를 구하는 함수

    Args:
        a (int): 최대공약수를 구할 정수 1
        b (int): 최대공약수를 구할 정수 2
    Returns:
        int: a와 b의 최대공약수
    """
    a, b = (a, b) if a > b else (b, a)
    g = 0
    while b > 0:
        g = a % b
        a = b
        b = g

    return a


def lcm(a: int, b: int):
    """최소공배수를 구하는 함수

    Args:
        a (int): 최소공배수를 구할 정수 1
        b (int): 최소공배수를 구할 정수 2
    Returns:
        int: a와 b의 최소공배수
    """
    g = gcd(a, b)
    l = a * b // g

    return l


a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
