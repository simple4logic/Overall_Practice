#include <bits/stdc++.h>
using namespace std;

int main(){
    int ans=0, x=0;
    char n;
    while(~scanf("%c", &n)){
        if(n==' '){
            if(x==0)
                cout<<"first filtering\n";
            else
                ans++;
        }
        x=1;
    }
    if(n == '\0') {cout << "zero word\n" ;printf("0"); return 0;} //zero word filtering
    if(n==' ')
        {ans--;cout<<"last filtering\n";} 
    printf("%d", ans+1);
}