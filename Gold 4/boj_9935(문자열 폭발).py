#input = sys.stdin.readline을 처음 써본 문제
#문자열을 스택에 넣어서 만약 문자의 끝 == 폭발 문자열의 끝일때 폭발 문자열의 길이 범위 내로 검사해서 폭발시키면서 진행
import sys
input = sys.stdin.readline
string = input().rstrip("\n")
bomb = list(input().rstrip("\n"))
blen = len(bomb)
stack = []
for i in string:
    stack.append(i)
    if i == bomb[-1]:
        if stack[-blen:] == bomb:
            del stack[-blen:]
print(*stack if stack else "FRULA", sep="")
