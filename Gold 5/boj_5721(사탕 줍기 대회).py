#예시로 중간을 처음 선택한다는 점에서 좀 혼란이 오다가 중간 줄부터 먼저 선택하든 첫 번째 세로줄 부터 선택하든 상관이 없다는 것을 깨달음
#어쨌든 며칠 동안 고민해봐서 재밌었던 문제
#maxcandy[i] = max(maxcandy[i - 2], maxcandy[i - 3]) + plus
#plus = max(dp[i])
#dp[i][j] = (i번째 줄에서 j번째 열까지 탐색했을 떄 얻는 사탕의 최댓값)
import sys
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == m == 0:
        break
    mpg = [[0 for _ in range(m + 1)]] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    maxcandy = [0 for _ in range(n + 1)]
    ans = -float('inf')
    for i in range(1, n + 1):
        dp = [0 for _ in range(m + 1)]
        plus = -float('inf')
        for j in range(1, m + 1):
            if j < 3:
                dp[j] = mpg[i][j]
            else:
                dp[j] = max(dp[j - 2], dp[j - 3]) + mpg[i][j]
            plus = max(plus, dp[j])
        if i < 3:
            maxcandy[i] = plus
            ans = max(ans, maxcandy[i])
        else:
            maxcandy[i] = max(maxcandy[i - 2], maxcandy[i - 3]) + plus
            ans = max(ans, maxcandy[i])
    print(ans)
