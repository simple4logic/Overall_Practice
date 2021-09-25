#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b;
    cin >> a;
    int mx=-1000000;
    int mn=1000000;
    while(a--){
        cin >> b;
        mx = max(b, mx);
        mn = min(b, mn);
    }
    printf("%d %d", min, max);
}