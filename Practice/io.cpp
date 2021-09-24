#include<iostream>
using namespace std;

int main(){
    char str[11];
    int a;
    while((a =scanf("%10s", &str))==1){
        printf("scanf return : %d\n", a);      
        cout << str << endl;
    }

    printf("last scanf return value : %d\n", a);
}