"""27982.py
Title: 큐브 더미
Url: https://www.acmicpc.net/problem/27982
"""

op = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]


N, M = map(int, input().split())
cube_dict = {}
for _ in range(M):
    input_cube = tuple(map(int, input().split()))
    cube_dict[input_cube] = True

cnt = 0
for x, y, z in cube_dict.keys():
    if (
        cube_dict.get((x - 1, y, z))
        and cube_dict.get((x + 1, y, z))
        and cube_dict.get((x, y - 1, z))
        and cube_dict.get((x, y + 1, z))
        and cube_dict.get((x, y, z - 1))
        and cube_dict.get((x, y, z + 1))
    ):
        cnt += 1

print(cnt)
