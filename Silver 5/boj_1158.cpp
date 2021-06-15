//������ ���� C++�� ���� �� Ǭ ����
//�׳� ������ ���� ������, k��°�� �ƴ� ��� ť�� �ٽ� ���Ҹ� �ְ�, �ƴϸ� ����� �� �ٽ� ��� ������ �Ǵ� ����
#include<iostream>
#include<queue>
using namespace std;
int main(){
    int N,K;
    cin >> N;
    cin >> K;
    queue<int> q;
    for (int i=1;i<=N;i++){
        q.push(i);
    }
    int temp;
    cout << "<";
    while (N--){
        temp = 0;
        for (int i=1;i<=K;i++){
            temp = q.front();
            if (i==K){
                q.pop();
                cout << temp ;
                if (N!=0) cout << ", ";
            }
            else{
                q.pop();
                q.push(temp);    
            }
        }
    }
    cout << ">";
    return 0;
}