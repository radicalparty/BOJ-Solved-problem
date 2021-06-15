#python�� ��ųʸ��� �ΰ� ���� Ǭ ����
#���� i��°�� j��� ���ڿ��� ������ dict1[i] = j, dict2[j] = i �̷� ������ ǰ
#�Է��� ���ڿ��� ���ڰ� ���ÿ� ������, �� �Է��� �� �� ���� ��Ȳ�� ������ ������ try - except���� ����� �ذ�
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