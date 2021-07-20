#발상은 10분 만에 했으나 처리가 고생이었던 문제
#x좌표들의 차를 구한 뒤 양이면 왼쪽으로, 음이면 오른쪽으로 당기면서 하고, 중앙과 나머지 세 좌표 중 가장 짧은 거리를 찾으면 되는 문제
import sys
M, N, L = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
x.sort()
ans = 0
for i in animal:
    posx, posy = i
    st, end = 0, M - 1#mid == 1(x[mid] = 4)
    while st <= end:
        mid = (st + end) // 2
        if x[mid] < posx:
            st = mid + 1
        else:
            end = mid - 1
    one = two = three = float('inf')
    two = x[mid]
    if mid > 0:
        one = x[mid - 1]
    if mid < M - 1:
        three = x[mid + 1]
    k = min((abs(posx - one), abs(posx - two), abs(posx - three)))
    if k + posy <= L:
        ans += 1
print(ans)
