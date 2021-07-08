#마을을 최소 특정 갯수의 집으로 만들 필요 없으므로 그냥 최소 스패닝 트리를 구한 뒤 가장 큰 간선을 빼면 그게 정답(순환하지 않으므로 하나만 끊어도 됨)
import sys
v, e = map(int, sys.stdin.readline().split())
w = []
parent = [_ for _ in range(v + 1)]
for i in range(e):
    st, end, weight = map(int, sys.stdin.readline().split())
    w.append([weight, st, end])
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
w.sort()
cnt = ans = cntrun = 0
while cnt < v - 2:
    weight, x, y = w[cntrun]
    t1, t2 = find(x), find(y)
    if t1 != t2:
        union(x, y)
        ans += weight
        cnt += 1
    cntrun += 1
print(ans) 
