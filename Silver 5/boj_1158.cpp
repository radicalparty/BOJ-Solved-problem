//예전에 내가 C++을 썼을 때 푼 문제
//그냥 간단한 구현 문제로, k번째가 아닐 경우 큐에 다시 원소를 넣고, 아니면 출력한 후 다시 계속 돌리면 되는 문제
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