#Greedy
#1 - n + 1 안에서 합은 어디서나 존재 가능 하므로 더해주면서 넘으면 끝
import sys
n = int(sys.stdin.readline())
total = 0
for i in range(1, n + 1):
    total += i
    if total > n:
        print(i - 1)
        break 
