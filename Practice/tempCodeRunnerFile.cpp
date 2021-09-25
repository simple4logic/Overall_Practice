#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, b;
    cin >> n;

    for(b=0;b<n;b++){
        for(int i=0;i<n-b+1;i++){
            printf(" ");
        } 
        for(int j=0;j<b+1;j++){
            printf("* ");
        }
        printf("\n");
    }
}