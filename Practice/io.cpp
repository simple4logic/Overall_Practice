#include<iostream>
using namespace std;

int main(){
    int n;
    int cnt = 0;
    cin >> n;

    while(n!=1){
        if(n%3==0){
            n/=3;
            cnt++;
            printf("used 3division\n");
            continue;
                    }
        if(n%2==0){
            n/=2;
            cnt++;
            printf("used 2division\n");
            continue;
        }
        n--;
        printf("used 1minus\n");
        cnt++;
    }
    printf("%d\n", cnt);
}