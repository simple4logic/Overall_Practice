#include<iostream>
using namespace std;
int main(){
    int T,a;
    int sum=0;
    cin >> T;
    while(T--){
        scanf("%1d", &a);
        sum +=a;
    }
    cout << sum;
}