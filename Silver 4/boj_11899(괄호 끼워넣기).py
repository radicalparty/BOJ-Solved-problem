#굳이 스택 쓸 필요 없는 문제
import sys
string = list(sys.stdin.readline().rstrip("\n"))
left = 0
cnt = 0
for i in string:
    if i == ")":
        if left == 0:
            cnt += 1
        else:
            left -= 1
    else:
        left += 1
print(cnt + left)
