#Dynamic Programming
import sys
n = int(sys.stdin.readline())
opendoor = list(map(int, sys.stdin.readline().split()))
query = int(sys.stdin.readline())
dp = [[[float('inf') for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(query + 1)]
qlist = [0] + [int(sys.stdin.readline()) for _ in range(query)]
dp[0][opendoor[0]][opendoor[1]] = dp[0][opendoor[1]][opendoor[0]] = 0
mini = float('inf')
for t in range(1, query + 1):
    destination = qlist[t]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            movei, movej = abs(destination - i), abs(destination - j)
            dp[t][i][destination] = dp[t][destination][i] = min(dp[t][i][destination], dp[t - 1][i][j] + movej)
            dp[t][j][destination] = dp[t][destination][j] = min(dp[t][j][destination], dp[t - 1][i][j] + movei)
            if t == query:
                mini = min(mini, dp[t][i][destination], dp[t][j][destination])
print(mini)
