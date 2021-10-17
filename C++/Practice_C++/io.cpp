#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,a=0;
    scanf("%d", &n);
    switch(n%5){
    case 0:
        a=n/5;
        break;
    case 1:
        a=n/5+1;
    case 2:
        if(n==7)
            a=-1;
        else
            a=n/5 +2;
        break;
    case 3:
        a =n/5+1;
        break;
    case 4:
        if(n==4)
            a=-1;
        else
            a=n/5+2;
        break;
    }
    printf("%d",a);
 }

 