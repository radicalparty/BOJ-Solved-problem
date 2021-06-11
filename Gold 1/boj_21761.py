import sys, heapq
def func(a, b, c, d):
    round1 = ([a, "A"] if a >= b else [b, "B"])
    round2 = ([c, "C"] if c >= d else [d, "D"])
    final = (round1 if round1[0] >= round2[0] else round2)
    return final[1]
carda = []
cardb = []
cardc = []
cardd = []
lena = lenb = lenc = lend = 0
n, k = map(int, sys.stdin.readline().split())
A, B, C, D = map(int, sys.stdin.readline().split())
for i in range(n):
    x, y = sys.stdin.readline().split()
    y = int(y)
    if x == "A":
        heapq.heappush(carda, -y)
        lena += 1
    elif x == "B":
        heapq.heappush(cardb, -y)
        lenb += 1
    elif x == "C":
        heapq.heappush(cardc, -y)
        lenc += 1
    else:
        heapq.heappush(cardd, -y)
        lend += 1
for i in range(k):
    if lena == 0:
        a = 0
    else:
        a = -carda[0] * B * C * D
    if lenb == 0:
        b = 0
    else:
        b = -cardb[0] * A * C * D
    if lenc == 0:
        c = 0
    else:
        c = -cardc[0] * A * B * D
    if lend == 0:
        d = 0
    else:
        d = -cardd[0] * A * B * C
    pos = func(a, b, c, d)
    if pos == "A":
        print("A {}".format(-carda[0]))
        A += -carda[0]
        heapq.heappop(carda)
        lena -= 1
    elif pos == "B":
        print("B {}".format(-cardb[0]))
        B += -cardb[0]
        heapq.heappop(cardb)
        lenb -= 1
    elif pos == "C":
        print("C {}".format(-cardc[0]))
        C += -cardc[0]
        heapq.heappop(cardc)
        lenc -= 1
    else:
        print("D {}".format(-cardd[0]))
        D += -cardd[0]
        heapq.heappop(cardd)
        lend -= 1