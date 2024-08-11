"""2798.py
Title: 블랙잭
Url: https://www.acmicpc.net/problem/2798
"""


def get_max_card_sum(N: int, M: int, cards: list):
    """M을 넘지 않는 3개 수의 최댓값을 구하는 함수

    Args:
        N (int): cards의 길이
        M (int): 넘으면 안되는 수
        cards (list): 숫자 리스트

    Returns:
        int: M을 넘지 않는 3개 수의 최댓값
    """
    max_sum = 0
    for i in range(N - 2):
        if cards[i] >= M:
            return max_sum
        for j in range(i + 1, N - 1):
            if cards[i] + cards[j] >= M:
                return max_sum
            for k in range(j + 1, N):
                card_sum = cards[i] + cards[j] + cards[k]
                if card_sum == M:
                    return card_sum
                elif card_sum < M:
                    max_sum = max(max_sum, card_sum)
                else:
                    break

    return max_sum


N, M = map(int, input().split())
cards = sorted([*map(int, input().split())])

max_sum = get_max_card_sum(N, M, cards)

print(max_sum)
