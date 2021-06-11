n, k = map(int,input().split())
dp = [[0]*(k+1) for i in range(n+1)]
for i in range(0,n+1):
    dp[i][1] = 1 
for i in range(2,k+1):
    for j in range(0,n+1):
        for u in range(0,j+1):
            dp[j][i] += dp[j-u][i-1]
            if dp[j][i] > 1000000000:
                dp[j][i] = dp[j][i] % 1000000000
print(dp[-1][-1]) 