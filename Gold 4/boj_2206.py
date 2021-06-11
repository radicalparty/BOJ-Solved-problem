#BFS(breadth - first search)문제
#처음 백준 풀었을때와 지금 이 문제를 풀 때 이 문제가 쉽게 느껴지는 걸 보니 나도 어느 정도는 성장함을 느낌
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
mpg = [['1' for _ in range(m + 1)]] + [['1'] + list(sys.stdin.readline().rstrip("\n")) for _ in range(n)]
visit = [[[False, False] for _ in range(m + 1)] for _ in range(n + 1)]
def bfs(mpg, visit):
    ans = -1
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    queue = deque()
    queue.append([1, 1, 1, 0])
    while queue:
        x, y, d, ck = queue.popleft()
        if x == n and y == m:
            ans = d
            return ans 
        if visit[x][y][ck]:
            continue
        visit[x][y][ck] = True
        for i in range(4):
            newx, newy = x + dx[i], y + dy[i]
            if newx < 1 or newy < 1 or newx > n or newy > m:
                continue 
            if mpg[newx][newy] == "1":
                if ck == 1:
                    continue
                else:
                    queue.append([newx, newy, d + 1, 1])
            else:
                queue.append([newx, newy, d + 1, ck])
    return ans
print(bfs(mpg, visit))
