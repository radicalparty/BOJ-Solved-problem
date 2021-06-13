#1차원 bfs문제, 딱히 어렵지는 않음
#repl에서 시간 걸려서 시간초과 날 줄 알았던 문제기도 함
#visit[x]에 x까지 가는데 걸리는 최소 시간 저장 후 b에 저장해둔 도착지 visit[x]와, 시간이 같을 경우 ans에 1을 더해주고, 시간이 넘으면 return 해주는 식으로 풀음
import sys
from collections import deque
a, b = map(int, sys.stdin.readline().split())
def bfs(a, b):
    ans = 0
    queue = deque()
    queue.append([a, 0])
    visit = [float('inf') for _ in range(150001)]
    while queue: 
        x, y = queue.popleft()
        if x < 0 or x >= 150001:
            continue
        if x == b:
            if visit[x] < y:
                return visit[x], ans
            else:
                visit[x] = y
                ans += 1 
        elif y > visit[x]:
            continue
        else:
            visit[x] = y
            queue.append([x - 1, y + 1])
            queue.append([x + 1, y + 1])
            queue.append([2 * x, y + 1])
    return visit[b], ans
v1, v2 = bfs(a, b)
print(v1)
print(v2)
