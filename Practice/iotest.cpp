#include <bits/stdc++.h>
using namespace std;

int main(){
    int ans=0, x=0; //문자 사이의 공백 수
    char n;
    while(~scanf("%c", &n)){
        if(n==' '){
            if(x==0) // 맨 첫번째 공백 filtering
                cout << "first filter activated"<<endl;
            else
                ans++;
        }
        x=1; //첫 입력 끝나면 더이상 first filter X
    }
    if(n==' '){
        ans--; 
        cout << "last filter activated"<< endl;
    }
    printf("%d", ans+1);
}