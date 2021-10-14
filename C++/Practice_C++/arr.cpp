#include <bits/stdc++.h>
using namespace std;

int f(char x);

int main(){
    char n;
    int sum = 0;
    while(~scanf(" %c", &n)){
        sum+=f(n);
    }
    printf("%d", sum);    
}

int f(char x){
    int y = 0;
    if(x>86)
        y++;
    if(x>83)
        y++;
    if(x>79)
        y++;
    if(x>76)
        y++;
    if(x>73)
        y++;
    if(x>70)
        y++;
    if(x>67)
        y++;
    y+=3;
    return y; 
}