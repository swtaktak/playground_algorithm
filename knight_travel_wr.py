# 나이트의 이동
mv = [[-2, -1], [-1, -2], [1, -2], [2, -1],
      [2, 1], [1, 2], [-1, 2], [-2, 1]]

def warnsdorff_rule(i, j):
    """Warnsdorff's Rule에 따라 이동 가능한 위치의 수를 기준으로 정렬"""
    moves = []
    for dx, dy in mv:
        nx, ny = i + dx, j + dy
        if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and board[nx][ny] == 0:
            count = 0
            for ddx, ddy in mv:
                nnx, nny = nx + ddx, ny + ddy
                if 0 <= nnx < rows and 0 <= nny < cols and not visited[nnx][nny] and board[nnx][nny] == 0:
                    count += 1
            moves.append((count, nx, ny))
    moves.sort()  # 이동 가능한 칸이 적은 순서로 정렬
    return [(nx, ny) for _, nx, ny in moves]

def dfs(depth, i, j):
    global max_knight, answer_visited
    # 최대 깊이 갱신
    if depth > max_knight:
        max_knight = depth
        answer_visited = [row[:] for row in visited]  # 정답 갱신

    # Warnsdorff's Rule에 따라 이동
    for nx, ny in warnsdorff_rule(i, j):
        visited[nx][ny] = depth + 1
        dfs(depth + 1, nx, ny)
        visited[nx][ny] = 0  # 백트래킹

# 입력
rows, cols = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(rows)]

# 변수 초기화
visited = [[0] * cols for _ in range(rows)]
answer_visited = [[0] * cols for _ in range(rows)]
max_knight = 0

# 모든 칸에서 시도
for i in range(rows):
    for j in range(cols):
        if board[i][j] == 0:
            visited[i][j] = 1
            dfs(1, i, j)
            visited[i][j] = 0

# 결과 출력
for row in answer_visited:
    print(" ".join(map(str, row)))
