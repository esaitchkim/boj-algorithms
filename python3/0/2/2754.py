"""2754.py
Title: 학점계산
Url: https://www.acmicpc.net/problem/2754
"""

grade_dict = {}
grade_dict["A+"], grade_dict["A0"], grade_dict["A-"] = 4.3, 4.0, 3.7
grade_dict["B+"], grade_dict["B0"], grade_dict["B-"] = 3.3, 3.0, 2.7
grade_dict["C+"], grade_dict["C0"], grade_dict["C-"] = 2.3, 2.0, 1.7
grade_dict["D+"], grade_dict["D0"], grade_dict["D-"] = 1.3, 1.0, 0.7
grade_dict["F"] = 0.0

grade_c = input()
score_c = grade_dict.get(grade_c)

print(score_c)
