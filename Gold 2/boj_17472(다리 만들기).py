#implementation & bfs & dfs & union-find
#union-find에서 조심할 것!
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
mpg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
ans = cnt = 0
count = 0
def mapmakingbfs(i, j, color):
    queue = deque()
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        visit[x][y] = True
        mpg[x][y] = color
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if mpg[nx][ny] == 0 or visit[nx][ny]:
                continue
            queue.append([nx, ny])
for i in range(n):
    for j in range(m):
        if mpg[i][j] != 0 and (visit[i][j] == False):
            cnt += 1
            mapmakingbfs(i, j, cnt)
parent = [_ for _ in range(cnt + 1)]
graph = [[float('inf') for _ in range(cnt + 1)] for _ in range(cnt + 1)]
def dfs(i, j, color):
    stack = deque()
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    stack.append([i, j, 0, 0])
    stack.append([i, j, 1, 0])
    stack.append([i, j, 2, 0])
    stack.append([i, j, 3, 0])
    while stack:
        x, y, direct, d = stack.pop()
        if d == 0:
            nx, ny = x + dx[direct], y + dy[direct]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            stack.append([nx, ny, direct, d + 1])
            continue
        if mpg[x][y] and mpg[x][y] != color:
            if d == 2:
                continue
            graph[color][mpg[x][y]] = graph[mpg[x][y]][color] = min(graph[mpg[x][y]][color], d - 1)
        elif mpg[x][y] == color:
            continue
        else:
            nx, ny = x + dx[direct], y + dy[direct]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            stack.append([nx, ny, direct, d + 1])
for i in range(n):
    for j in range(m):
        if mpg[i][j]:
            dfs(i, j, mpg[i][j])
edge = []
for i in range(1, cnt + 1):
    for j in range(1, i):
        if graph[i][j] != float('inf'):
            edge.append([graph[i][j], j, i])
edge.sort()
def find(i):
    if i == parent[i]:
        return i
    parent[i] = find(parent[i])
    return parent[i]
def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
for node in edge:
    w, st, end = node
    t1, t2 = find(st), find(end)
    if t1 == t2:
        continue
    ans += w
    count += 1
    if count == cnt - 1:
        break
    union(st, end)
print(ans if count == cnt - 1 else -1)
