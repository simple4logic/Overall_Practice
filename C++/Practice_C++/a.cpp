#include <bits/stdc++.h>
using namespace std;

void division(int x);

int main(){
    int n;
    scanf("%d", &n);
    division(n);
    return 0;
 }

 void division(int x){
    if(x==1) //exit of recursion // case1 input is 1 or end of recursion.
        exit(0);

    for(int i=2;i<=x;i++){ // if x =3
        if(x%i==0){//if divided by i
            x = x/i;
            printf("%d\n", i);
            //printf("now x: %d\n", x);
            division(x);
        }
    }
 }