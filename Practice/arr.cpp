#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> a(26);
    int i=0, max=0, id=0;
    string let;
    cin >> let;
    transform(let.begin(), let.end(), let.begin(), ::toupper);
    while(let[i]){
        int temp = let[i];
        a[temp-65]++;
        i++;
    }
    i =0;
    for(auto N:a){
        if(a[i]!=0)if(max == a[i])id = -1;
        if(max < a[i]){
            max = a[i];
            id = i;
        }
        i++;
    }
    if(id == -1)
        printf("?");
    else
        printf("%c", 65+id);
}