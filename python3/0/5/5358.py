"""5358.py
Title: Football Team
Url: https://www.acmicpc.net/problem/5358
"""

trans_table = str.maketrans("ieIE", "eiEI")

while True:
    try:
        player = input()
        player = player.translate(trans_table)
        print(player)
    except:
        break
