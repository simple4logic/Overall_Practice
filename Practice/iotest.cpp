#include <bits/stdc++.h>
using namespace std;

int cbn(int n, int r)
{
    if(n == r || r == 0) 
        return 1; 
    else 
        return cbn(n - 1, r - 1) + cbn(n - 1, r);
}

int main(){
    int x;
    int y=0;
    int sum=0;
    cin >> x;
    while(x>y){
        sum+=cbn(x, y);
        x--; y++;
    }

    printf("%d", sum%1007);
}
