#13392번 문제의 재탕이 강하게 의심되는 문제
#13392에다 track[i][j]라는 역추적 배열을 만들고 경우에 따라 저장하고 역추적 하면 문제 끝
import sys
n = int(sys.stdin.readline())
dp = [[float('inf') for _ in range(10)] for _ in range(n + 1)]#n번째 나사가 총 i번 돌려졌을 때 돌려진 최솟값(i = i % 10)
track = [[(0, 0, 0) for _ in range(10)] for _ in range(n + 1)]
num1 = [0] + list(sys.stdin.readline().rstrip("\n"))
num2 = [0] + list(sys.stdin.readline().rstrip("\n"))
ans = float('inf')
for i in range(1, n + 1):
    st = int(num1[i])
    end = int(num2[i])
    if i == 1:
        if st < end:
            dp[i][end - st] = (end - st)#왼쪽 회전
            dp[i][0] = (10 + st - end)#오른쪽 회전, 수의 감소
            track[i][end - st] = (0, 0, end - st)
            track[i][0] = (0, 0, - 10 - st + end)
        elif st == end:
            dp[i][0] = 0
        else:#st > end
            dp[i][0] = (st - end)#오른쪽 회전, 수의 감소
            dp[i][10 + end - st] = (10 + end - st) 
            track[i][0] = (0, 0, - st + end)
            track[i][10 + end - st] = (0, 0, 10 + end - st)
        continue
    for j in range(0, 10):
        x = (st + j if st + j < 10 else st + j - 10)#회전한 정도에 따라 현재 num1[i]의 좌표 추적
        if x <= end:#현재 위치가 end 보다 작을 때
            move = (end - x) % 10
            plus = (j + end - x) % 10
            a = dp[i][j]
            b = dp[i][plus]
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 10 - move) #오른쪽으로 돌릴 때(밑 나사 회전 안함)), 숫자 감소
            dp[i][plus] = min(dp[i][plus], dp[i - 1][j] + move)#왼쪽으로 돌릴 때: 밑 나사 회전함, 숫자 증가
            if dp[i][j] != a:
                track[i][j] = (i - 1, j, -10 + move)
            if dp[i][plus] != b:
                track[i][plus] = (i - 1, j, move)
        else:# x > end
            move = (10 + end - x) % 10#좌회전
            plus = (j + move) % 10
            a = dp[i][j]
            b = dp[i][plus]
            dp[i][plus] = min(dp[i][plus], dp[i - 1][j] + move)#왼쪽으로 돌릴 때
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 10 - move)#오른쪽으로 돌릴 때
            if dp[i][j] != a:
                track[i][j] = (i - 1, j, -10 + move)
            if dp[i][plus] != b:
                track[i][plus] = (i - 1, j, move)
pos = 0
for i in range(0, 10):
    c = ans
    ans = min(ans, dp[n][i])
    if c != ans:
        pos = i
print(ans)
poslist = []
cnt = n
while cnt != 0:
    a, b, c = track[cnt][pos]
    cnt -= 1
    poslist.append(c)
    pos = b
poslist = poslist[::-1]
cnt = 1
for i in poslist:
    print("{} {}".format(cnt, i))
    cnt += 1 
