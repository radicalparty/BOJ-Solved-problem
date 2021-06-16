#BFS(Breadth first Search), Brute Force(10이상은 -1로 처리한다는 조건에 의해)임은 쉽게 알 수 있으나 구현이 힘들었던 문제
#4^10번을 검사해서 bfs를 실행, 두 구슬 전부 움직이지 않는 경우와 visit[rx][ry][bx][by]라는 4차원 배열로 중복을 처리하면 많은 경우를 실행하지 않아도 됨
#구슬 탈출 1, 2
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
mpg = [list(sys.stdin.readline().rstrip("\n")) for _ in range(n)]
visit = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
#rx, ry, bx, by
for i in range(n):
    for j in range(m):
        if mpg[i][j] == "B":
            bx, by = i, j
            mpg[bx][by] = "."
        elif mpg[i][j] == "R":
            rx, ry = i, j
            mpg[rx][ry] = "."
def move(ax, ay, direct):
    if direct == 0:#left
        for i in range(ay, 0, -1):
            if mpg[ax][i - 1] == "O":
                return ax, i - 1, True
            elif mpg[ax][i - 1] == "#":
                return ax, i, False
    elif direct == 1:#right
        for i in range(ay, m - 1):
            if mpg[ax][i + 1] == "#":
                return ax, i, False
            elif mpg[ax][i + 1] == "O":
                return ax, i + 1, True
    elif direct == 2:#up
        for i in range(ax, 0, -1):
            if mpg[i - 1][ay] == "#":
                return i, ay, False
            elif mpg[i - 1][ay] == "O":
                return i - 1, ay, True
    elif direct == 3:#down
        for i in range(ax, n - 1):
            if mpg[i + 1][ay] == "#":
                return i, ay, False
            elif mpg[i + 1][ay] == "O":
                return i + 1, ay, True  
def newpos(rx, ry, bx, by, direct):
    end1 = end2 = False
    k = (0, 0, 0, 0, 2)
    if direct == 0:#left
        if ry <= by:
            rx, ry, end1 = move(rx, ry, direct)
            mpg[rx][ry] = "#" if end1 == False else "O"
            bx, by, end2 = move(bx, by, direct)
            mpg[rx][ry] = "." if end1 == False else "O"
        else:
            bx, by, end2 = move(bx, by, direct)
            if end2:
                return k
            mpg[bx][by] = "#"
            rx, ry, end1 = move(rx, ry, direct)
            mpg[bx][by] = "."
    elif direct == 1:#right
        if ry >= by:
            rx, ry, end1 = move(rx, ry, direct)
            mpg[rx][ry] = "#" if end1 == False else "O"
            bx, by, end2 = move(bx, by, direct)
            mpg[rx][ry] = "." if end1 == False else "O"
        else:
            bx, by, end2 = move(bx, by, direct)
            if end2:
                return k
            mpg[bx][by] = "#"
            rx, ry, end1 = move(rx, ry, direct)
            mpg[bx][by] = "." 
    elif direct == 2:#up
        if rx <= bx:
            rx, ry, end1 = move(rx, ry, direct)
            mpg[rx][ry] = "#" if end1 == False else "O"
            bx, by, end2 = move(bx, by, direct)
            mpg[rx][ry] = "." if end1 == False else "O"
        else:
            bx, by, end2 = move(bx, by, direct)
            if end2:
                return k
            mpg[bx][by] = "#"
            rx, ry, end1 = move(rx, ry, direct)
            mpg[bx][by] = "."
    else:#down
        if rx >= bx:
            rx, ry, end1 = move(rx, ry, direct)
            mpg[rx][ry] = "#" if end1 == False else "O"
            bx, by, end2 = move(bx, by, direct)
            mpg[rx][ry] = "." if end1 == False else "O"
        else:
            bx, by, end2 = move(bx, by, direct)
            if end2:
                return k
            mpg[bx][by] = "#"
            rx, ry, end1 = move(rx, ry, direct)
            mpg[bx][by] = "."
    if end2:
        return k
    elif end1:
        end = 1
    else:
        end = 0
    return rx, ry, bx, by, end     
def answer(x, y, x1, y1):
    ans = -1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
#차례대로 left, right, up, down
    queue = deque()
    queue.append([0, x, y, x1, y1])
    while queue:
        d, rx, ry, bx, by = queue.popleft()
        if visit[rx][ry][bx][by]:
            continue
        visit[rx][ry][bx][by] = True
        if d >= 10:
            break
        for i in range(4):
            if mpg[rx + dx[i]][ry + dy[i]] == "#" and mpg[bx + dx[i]][by + dy[i]] == "#":
                continue
            xr, yr, xb, yb, end = newpos(rx, ry, bx, by, i)
            if end == 2:
                continue
            elif end == 1:
                return d + 1
            else:
                queue.append([d + 1, xr, yr, xb, yb])
    return -1
print(answer(rx, ry, bx, by))
