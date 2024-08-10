"""2920.py
Title: 음계 
Url: https://www.acmicpc.net/problem/2920
"""

input_string = input()
ascending = "1 2 3 4 5 6 7 8"
descending = "8 7 6 5 4 3 2 1"

result = "mixed"

if input_string == ascending:
    result = "ascending"
elif input_string == descending:
    result = "descending"

print(result)
