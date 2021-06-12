#implementation, queue문제
#현재 있는 위치를 큐에 넣고 만약 먹으면 그대로 두고, 먹지 않으면 넣은 것중 처음에 존재하던 것을 빼주면서 배열에서 뱀 꼬리를 제거하는 게임
#발전의 성과 2
import sys
from collections import deque
n = int(sys.stdin.readline())
mpg = [[1 for _ in range(n + 2)]] + [[1] + [0 for _ in range(n)] + [1] for _ in range(n)] + [[1 for _ in range(n + 2)]]
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    mpg[x][y] = 2
order = int(sys.stdin.readline())
cmd = []
for _ in range(order):
    t, string = sys.stdin.readline().split()
    t = int(t)
    cmd.append([t, string])
queue = deque()#1: right, 2: down, 3: left, 4: up
t = 0
count = 0
def directchange(direct, string):
    if string == "D":
        if direct == 4:
            return 1
        else:
            return direct + 1
    else:
        if direct == 1:
            return 4
        else:
            return direct - 1
x, y, direct = 1, 1, 1
queue.append([1, 1])
while True:
    if count >= order:
        count = count
    elif t == cmd[count][0]:
        direct = directchange(direct, cmd[count][1])
        count += 1
    if direct == 1:#right
        x, y, direct = x, y + 1, direct
    elif direct == 2:#down
        x, y, direct = x + 1, y, direct
    elif direct == 3:#left
        x, y, direct = x, y - 1, direct
    else:#up
        x, y, direct = x - 1, y, direct
    t += 1
    queue.append([x, y])
    if mpg[x][y] == 1 or mpg[x][y] == 3:
        break
    elif mpg[x][y] == 0:
        dx, dy = queue.popleft()
        mpg[dx][dy] = 0
    mpg[x][y] = 3
print(t)
