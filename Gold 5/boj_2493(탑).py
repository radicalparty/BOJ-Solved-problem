#python이 느린데다 모든 범위를 검사하는 브루트 포스로 풀려 했기 때문에 한 번 시간초과 받고 맞춘 문제
#세 가지 경우로 구분함
#1) 현재 탑의 높이가 앞의 최댓값보다 클 때 => 스택 초기화, 최댓값을 현재로 변경하고 스택에 추가, 0 출력
#2) 현재 탑의 높이가 앞의 최댓값과 같을 때 => 스택 초기화, 최댓값은 현재로 변경하고 스택에 추가, 예전 최댓값 출력
#3) 현재 탑의 높이가 앞의 최댓값보다 작을 때 => 스택을 차례대로 빼면서 높이가 더 높으면 그 값을 출력하고 현재 높이를 스택에 추가 => 스택에서 나간 값은 현재 높이보다 더 낮으므로 반영할
# 필요 없음
import sys
stack = [0]
n = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
maxi = 1
for i in range(1, n + 1):
    top = num[i]
    if top > num[maxi] or i == 1:
        print(0, end = " ")
        maxi = i
        stack.clear()
        stack.append(i)
    elif top == num[maxi]:
        print(maxi, end = " ")
        maxi = i
        stack.clear()
        stack.append(i)
    else:
        ck = False
        while stack:
            x = stack.pop(-1)
            if num[x] >= top:
                print(x, end = " ")
                stack.append(x)
                stack.append(i)
                break
