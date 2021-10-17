#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,a=0;
    scanf("%d", &n);
    if(n%5==0)
        a = n/5;
    else if(n%5==1)
        a = n/5 +1;
    else if(n%5==2){
        if(n==7)
            a = -1;
        else
            a = n/5 +2;
    }
    else if(n%5==3)
        a = n/5 +1;
    else
        if(n==4)
            a=-1;
        else
            a =n/5+2;
    printf("%d", a);
 }

 