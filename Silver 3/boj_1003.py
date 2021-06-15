#Dynamic programming 문제
#처음에는 an((0을 호출하는 갯수) + (1을 호출하는 갯수)) = an, 즉 피보나치 수열인 줄 알았으나, 0과 1을 따로 계산하는 문제 
import sys
dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n][0], dp[n][1])