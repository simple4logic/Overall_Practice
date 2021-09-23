#include<iostream>
using namespace std;

int main(){
    int i;
    int j;
    char str[101];
    cin >> str;

    for(j=0;j<10;j++){
        for(i=0;i<10;i++){
            if(str[i+10*j]=='\0'){
                return 0;
            }
            printf("%c", str[i+10*j]);
        }
        cout << endl;
    }
}