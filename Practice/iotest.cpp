#include <iostream>
#include<string>
using namespace std;

int main(){
    int x[10]={};
    int n;
    int a=0;
    while(~scanf("%d",&n)){ //입력을 다받을 때까지
        x[a] = n%42;
        a++;
    } // 모든 나머지 배열 입력 완료
    
}

