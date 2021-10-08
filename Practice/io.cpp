#include <bits/stdc++.h>
using namespace std;

int main(){
    int ans=0, x=0;
    char n;
    while(~scanf("%c", &n)){
        if(n==' '){
            if(x==0)
                ;
            else
                ans++;
        }
        x=1;
    }
    if(n==' ')
        ans--; 
    printf("%d", ans+1);
}