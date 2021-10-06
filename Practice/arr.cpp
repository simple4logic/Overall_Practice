#include <iostream>
#include<memory.h>
using namespace std;

int main(){
    int alp[26], i=0;
    memset(alp, -1, sizeof(int)*26);
    string let;
    cin >> let;
    while(let[i]){
        int temp = let[i];
        if(alp[temp-97]==-1){
            alp[temp-97]=i;
        }
        i++;
    }
    for(int v : alp) printf("%d ", v);
}