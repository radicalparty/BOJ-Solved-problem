#jadu[i][j][k] = (i초에 j번 나무에 있고, k번 움직였을때, 먹을 수 있는 자두의 최댓값)
#어렵지는 않았으나 예외 처리를 좀 해야함
import sys
T, W = map(int, sys.stdin.readline().split())
maxi = 0
jadu = [0] + [int(sys.stdin.readline()) for _ in range(T)]
dp = [[[0 for _ in range(W + 1)] for _ in range(3)] for _ in range(T + 1)]
for i in range(1, T + 1):
    pos = jadu[i]
    for j in range(0, W + 1):
        if i < j:
            break
        elif i == 1:
            dp[i][1][0] = dp[i - 1][1][0] + (1 if pos == 1 else 0)
            dp[i][2][1] = dp[i - 1][1][0] + (1 if pos == 2 else 0)
            maxi = max(dp[i][1][0], dp[i][2][1], maxi)
            continue
        elif j == 0:
            dp[i][1][j] = dp[i - 1][1][j] + (1 if pos == 1 else 0)
            dp[i][2][j] = 0
            maxi = max(dp[i][1][j], maxi)
            continue 
        dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][2][j - 1]) + (1 if pos == 1 else 0)
        dp[i][2][j] = max(dp[i - 1][1][j - 1], dp[i - 1][2][j]) + (1 if pos == 2 else 0)
        maxi = max(dp[i][1][j], dp[i][2][j], maxi)
print(maxi)