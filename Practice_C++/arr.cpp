#include <bits/stdc++.h>
using namespace std;

int main(){
    int ans=0, x=0, c=0;
    char n;
    while(~scanf("%c", &n)){
        if(n==' '){
            if(x==0)
                ; //first filtering
            else
                ans++;
        }
        if(n!=' ')
            c++;
        x=1;
    }
    if((c==0)&&(ans==0)){printf("0"); return 0;} //zero word filtering
    if(n==' '){
        ans--; //last filtering
        if(c==0){
            printf("0");
            return 0;
        }
    }
    printf("%d", ans+1);
}