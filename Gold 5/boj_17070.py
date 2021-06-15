#파이프 옮기기 1, 2
#그냥 0: 수평, 1: 수직, 2: 대각선이라 하고 dp[i][j][direct] = i방향으로 파이프를 놓을 때 가능한 갯수를 dp로 처리해서 정답을 내면 되는 간단한 문제
import sys
n = int(sys.stdin.readline())
mpg = [[0 for _ in range(n + 1)]] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n + 1)] for _ in range(n + 1)]#0: 가로, 1: 세로, 2: 대각선
for i in range(1, n + 1):
    ck = 0
    for j in range(1, n + 1): 
        if i == 1 and j == 1:
            continue
        elif i == 1:
            if mpg[i][j] == 1 or ck == 1:
                ck = 1
            else:
                dp[i][j][0] = 1
        elif mpg[i][j] == 1:
            continue
        else:
            if mpg[i][j - 1] == 0:
                dp[i][j][0] += (dp[i][j - 1][0] + dp[i][j - 1][2])
            if mpg[i - 1][j - 1] == 0 and mpg[i - 1][j] == 0 and mpg[i][j - 1] == 0:
                dp[i][j][2] += (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2])
            if mpg[i - 1][j] == 0:
                dp[i][j][1] += (dp[i - 1][j][1] + dp[i - 1][j][2])
print(sum(dp[n][n]))   
