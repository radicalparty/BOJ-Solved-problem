#Dynamic Programming
#초반에 가장 위에만 있을때 상승 -> 하강 변화가 가능했다고 믿었던 실수
import sys
n, m = map(int, sys.stdin.readline().split())
if n == m == 1:
    n = int(sys.stdin.readline())
    print(n * 2)
    exit()
elif m == 1:
    mpg = [[0, 0]] + [[0, int(sys.stdin.readline())] for _ in range(n)]
else:
    mpg = [[0 for _ in range(m + 1)]] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]#dp[x][y], x = 위에서 볼때 거리, y = x좌표
maxi = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for x in range(n, 0, -1):
    for y in range(1, m + 1):
        if x == n:
            dp[x][y] = dp[x][y - 1] + mpg[x][y]
            continue 
        elif y == 1:
            dp[x][y] = dp[x + 1][y] + mpg[x][y]
            continue
        dp[x][y] = max(dp[x + 1][y], dp[x][y - 1]) + mpg[x][y]
for x in range(1, n + 1):
    for y in range(1, m + 1):
        if x == 1 and y == 1: 
            maxi[x][y] = dp[x][y] + mpg[x][y]
            continue
        elif x == 1:
            maxi[x][y] = max(dp[x][y], maxi[x][y - 1]) + mpg[x][y] 
            continue
        elif y == 1:
            maxi[x][y] = max(maxi[x - 1][y], dp[x][y]) + mpg[x][y]
            continue
        maxi[x][y] = max(maxi[x - 1][y], maxi[x][y - 1], dp[x][y]) + mpg[x][y]
print(maxi[-1][-1])
