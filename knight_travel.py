# Knight_travel
# 나이트를 가장 많이 옮길 수 있는 판이나 형태에 대해 연구해보기.
# 정사각형 판에 일부 벽을 준 다음에, 얼마나 많이 나이트가 점프 되나?
# 단, 한 번 간 곳은 안 가게.
# 0은 밟을 수 있는 칸, 1은 빈 칸.
# 5*5 백지만 해도 너무 오래 걸림... 더 좋게 할 수 없나?

import copy
mv = [[-2, -1], [-1, -2], [1, -2], [2, -1],
      [2, 1], [1, 2], [-1, 2], [-2, 1]]
def dfs(depth, i, j, visited):
    global max_knight
    global answer_visited
    if depth > max_knight:
        max_knight = depth
        answer_visited = copy.deepcopy(visited)
    for cur_mv in mv:
        nx, ny = i + cur_mv[0], j + cur_mv[1]
        if 0 <= nx < rows and 0 <= ny < cols:
            if visited[nx][ny] == 0 and board[nx][ny] == 0:
                visited[nx][ny] = depth + 1
                dfs(depth + 1, nx, ny, visited)
                visited[nx][ny] = 0
    return

rows, cols = map(int, input().split())
board = []
for _ in range(rows):
    cur_row = list(map(int, input().split()))
    board.append(cur_row)

answer_visited = [[0 for _ in range(cols)] for _ in range(rows)]
max_knight = 0
for i in range(rows):
    for j in range(cols):
        if board[i][j] == 0:
            visited = [[0 for _ in range(cols)] for _ in range(rows)]
            dfs(0, i, j, visited)

for i in range(rows):
    for j in range(cols):
        print(answer_visited[i][j], end = " ")
    print()