#disjoint set
#x, y 라는 두 개의 좌표로 union-find 연산을 처리해야 하는 문제
#총 그룹 수를 구한 뒤, 어느 두 집합은 하나의 스프링쿨러로 항상 합쳐 질 수 있다는 것에 주목해야 하는 문제
import sys
T = int(sys.stdin.readline())
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
for _ in range(T):
    n = groupnum = int(sys.stdin.readline())
    px = [False for _ in range(1000001)]
    py = [False for _ in range(1000001)]
    parent = [_ for _ in range(n + 1)]
    ck = -1
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        if px[x] and py[y]:#둘 다 존재 할 경우
            a, b = find(px[x]), find(py[y])
            if a == b:
                groupnum -= 1 
                ck = -1 
            else:
                union(px[x], py[y])
                groupnum -= 2
                ck = 0
            union(px[x], i + 1)
        elif px[x]:#하나만 존재 할 경우 
            py[y] = px[x]
            groupnum -= 1
            union(i + 1, px[x])
            ck = 1
        elif py[y]:
            px[x] = py[y] 
            groupnum -= 1
            union(i + 1, py[y])
            ck = 2
        else:
            px[x] = i + 1
            py[y] = i + 1
            ck = 3
    k = groupnum // 2
    if groupnum % 2 == 1:
        print(k + 1)
    else:
        print(k)
