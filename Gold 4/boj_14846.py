#문제 자체가 직설적이지 않아 좀 고민한 문제
#dp[i][j][k] = (i, j까지 k(1 - 10)이 누적된 횟수)
#dp[x2][y2][k] + dp[x1 - 1][y1 - 1][k] - dp[x1 - 1][y2][k] - dp[x2][y1 - 1][k]로 사각형 탐색, 안에 누적된 횟수가 0이면 넘어가고 누적된 횟수가 1 이상이면 1 더하는 방식으로 쿼리 처리
import sys
n = int(sys.stdin.readline())
mpg = [[0 for _ in range(n + 1)]] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[[0 for _ in range(11)] for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, 11):
            dp[i][j][k] += (dp[i - 1][j][k] + dp[i][j - 1][k] - dp[i - 1][j - 1][k])
        dp[i][j][mpg[i][j]] += 1
        
q = int(sys.stdin.readline())
for _ in range(q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    S = 0
    for k in range(1, 11):
        S += (1 if dp[x2][y2][k] + dp[x1 - 1][y1 - 1][k] - dp[x2][y1 - 1][k] - dp[x1 - 1][y2][k] else 0)  
    print(S)
