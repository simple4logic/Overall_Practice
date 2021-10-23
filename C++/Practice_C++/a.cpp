#include <bits/stdc++.h>
using namespace std;

int primegen(int max);

int main(){
    int n;
    while(n--){

    }
 }

 int primegen(int max){
    bool *test = new bool[max+1];
    for(int i=0;i<max+1;i++)
        test[i]=true;
    test[0]=false;
    test[1]=false;
    for(long int i=2;i<=max+1;i++){
        if(test[i]){
            for(long int j =i*i; j<=max+1;j+=i){
                test[j]= false;
            }
        }
    }

    for(int j=0;j<max+1;j++){
        if(test[j])
            printf("%d\n", j);
    }

    delete[] test;
 }