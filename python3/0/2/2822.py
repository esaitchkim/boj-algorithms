"""2822.py
Title: NAJBOLJIH 5
Url: https://www.acmicpc.net/problem/2822
"""

points_dict = {}

for i in range(1, 9):
    x = int(input())
    points_dict[x] = i

top_5_points = sorted(points_dict.keys(), reverse=True)[:5]
total_points = sum(top_5_points)
problems_no = [points_dict[i] for i in top_5_points]
problems_no.sort()
print(total_points)
print(*problems_no, sep=" ")
