#bfs 연습문제
import sys
from collections import deque
def dfs(i,j):
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    stack = deque()
    stack.append([i,j])
    while stack:
        x, y = stack.popleft()
        if x < 0 or x >= h or y < 0 or y >= w:
            continue
        if visit[x][y] == 1 or mpg[x][y] == 0:
            continue
        visit[x][y] = 1
        for i in range(4):
            stack.append([x + dx[i], y + dy[i]])
T = int(sys.stdin.readline())
for _ in range(T):
    w, h, k = map(int,sys.stdin.readline().split())
    mpg = [[0] * w for i in range(h)]
    visit = [[0] * w for i in range(h)]
    for _ in range(k):
        x, y = map(int,sys.stdin.readline().split())
        mpg[y][x] = 1
    cnt = 0
    for i in range(h):
        for j in range(w):
            if mpg[i][j] == 0 or visit[i][j] == 1:
                continue 
            cnt += 1 
            dfs(i,j)
    print(cnt)