#include <bits/stdc++.h>
using namespace std;

int main(){
    string str;
    int ans=0, len=0;
    while(cin.getline(str,'\n')){
        if(str[len]=' ')
            ans++;
        len++;
    }

    if(str[0]==' ') ans--;
    if(str[len]==' ') ans--;
}