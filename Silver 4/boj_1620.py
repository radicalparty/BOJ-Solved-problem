#python의 딕셔너리를 두개 만들어서 푼 문제
#만약 i번째에 j라는 문자열이 들어오면 dict1[i] = j, dict2[j] = i 이런 식으로 품
#입력이 문자열과 숫자가 동시에 들어오는, 즉 입력을 알 수 없는 상황이 나오기 때문에 try - except문을 사용해 해결
import sys
n, m = map(int, sys.stdin.readline().split())
dictionary1 = {}
dictionary2 = {}
for i in range(1, n + 1):
    string = sys.stdin.readline().rstrip("\n")
    dictionary1[string] = i
    dictionary2[i] = string
for j in range(1, m + 1):
    query = sys.stdin.readline().rstrip("\n")
    try:
        query = int(query)
        print(dictionary2[query])
    except:
        print(dictionary1[query])