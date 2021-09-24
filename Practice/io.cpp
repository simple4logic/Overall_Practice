#include<iostream>
using namespace std;

int main(){
    int a;
    int i =0;
    cin >> a;
    if(a>100000) return 0;
    while(i<a){
        cout << i+1 << endl;
        i++;
    }
}