#include <iostream>
using namespace std;
int scoring(char* a);
int main(){
    int n;
    scanf("%d", &n);
    while(n--){
        char arr[80]={};

        while(cin >> arr)
        printf("%d\n",scoring(arr));
    }
}
int scoring(char *a){
    int sum=0, x=0, y=0;
    while(a[x]!='\0'){
        y++;
        if(a[x]=='X')
            y=0;
        sum+=y;
        x++;
    }
    return sum;
}
