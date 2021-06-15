#스택 쓸 필요 없는 스택 문제, 스택 없는 스택 문제
#만약 "("이 오면 pair += 1, ")"이 올 때 pair -= 1 한뒤 전에 "("이면 레이저로 판단하고 ans += pair 전에 ")" 이면 막대로 판단하고 ans += 1로 처리함 
import sys
from collections import deque
pair = ans = 0
priority = " "
stack = list(sys.stdin.readline().rstrip("\n"))
for i in stack:
    if i == "(":
        pair += 1
    else:
        pair -= 1
        if priority == ")":
            ans += 1
        else:
            ans += pair
    priority = i
print(ans)
