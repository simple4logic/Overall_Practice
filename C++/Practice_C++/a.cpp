#include <bits/stdc++.h>
using namespace std;

int main(){
    int ans=0, x=0, c=0;
    char n;
    while((n=getchar())&&(n!='\n')){ //input until newline
        if(n==' '){
            if(x==0)
                ; //first filtering
            else
                ans++;
        }
        if(n!=' ') //to check whether letter emerged or not
            c++;
        x=1;
    }
    //if(n == '\0'){printf("0"); return 0;} //zero word filtering
    if(n==' '){ //ends with blank(=last word is blank)
        if(c==0)
            return 0; //when starts with blank, and ends with blank. this case word is zero.
        ans--; //last filtering
        printf("last filtering activated!\n");
    }
    printf("%d", ans+1);
}