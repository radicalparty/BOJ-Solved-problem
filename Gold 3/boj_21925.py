import sys
n = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1
    for j in range(i - 1, 0, -1):
        if j == i - 1 and num[j] == num[i]:
            dp[j][i] = 1
        elif num[i] == num[j] and dp[j + 1][i - 1] == 1:
            dp[j][i] = 1
ans = [-1] * (n + 1)
for i in range(2, n + 1, 2):
    if dp[1][i] == 1:
        ans[i] = 1
    for j in range(2, i - 1, 2):
        if ans[j] != -1 and dp[j + 1][i] == 1:
            ans[i] = max(ans[i], ans[j] + 1)
print(ans[-1])