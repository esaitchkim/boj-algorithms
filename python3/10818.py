"""10818.py
Title: 최소, 최대
Url: https://www.acmicpc.net/problem/10818
"""

# Solve 1
##################################################
N = int(input())

min_number = 1_000_000
max_number = -1_000_000

number_list = map(int, input().split())
for num in number_list:
    if num >= max_number:
        max_number = num
    if num <= min_number:
        min_number = num

print(f"{min_number} {max_number}")

##################################################


# Solve 2 - 메모리를 조금 더 절약하기 위한 방법
##################################################
def split_number(input_string: str):
    """입력받은 문자열을 공백 기준으로 나누어서 하나씩 yield

    Args:
        input_string (str): 입력받은 문자열, 각 숫자를 공백으로 구분

    Yields:
        number: 숫자
    """

    number = ""
    for c in input_string:
        if c == " ":
            if number:
                yield int(number)
                number = ""
        else:
            number += c

    if number:
        yield int(number)


N = int(input())
input_string = input()

min_number = 1_000_000
max_number = -1_000_000

for number in split_number(input_string):
    if number >= max_number:
        max_number = number
    if number <= min_number:
        min_number = number

print(f"{min_number} {max_number}")

##################################################
