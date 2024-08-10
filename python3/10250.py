"""10250.py
Title: ACM 호텔
Url: https://www.acmicpc.net/problem/10250
"""


def find_room_number(H: int, W: int, N: int):
    """층 수(H), 방 수(W), 손님 수(N)을 입력받아 해당 손님의 방 번호를 구한다.

    Args:
        H (int): 층 수
        W (int): 방 수
        N (int): 손님의 번호
    Returns:
        result (str): 손님의 방 번호
    """
    result_W = N // H if N % H == 0 else N // H + 1
    result_H = H if N % H == 0 else N % H
    result = str(result_H) + str(result_W).zfill(2)

    return result


T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    result = find_room_number(H, W, N)
    print(result)
