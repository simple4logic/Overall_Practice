#include <iostream>
#include<string>
using namespace std;

int main(){
    int n;
    int mul=1;
    string num;
    int ans[10]={};
    for(int i=0;i<3;i++){
        cin >> n;
        mul*=n;
    }
    num = to_string(mul);

    for(int j=0;j<10;j++){
        if(num[j]=='0')
            ans[0]++;
        if(num[j]=='1')
            ans[1]++;
        if(num[j]=='2')
            ans[2]++;
        if(num[j]=='3')
            ans[3]++;
        if(num[j]=='4')
            ans[4]++;
        if(num[j]=='5')
            ans[5]++;
        if(num[j]=='6')
            ans[6]++;
        if(num[j]=='7')
            ans[7]++;
        if(num[j]=='8')
            ans[8]++;
        if(num[j]=='9')
            ans[9]++;
    }
    int a=-1;
    while(a++<9){
        printf("%d\n", ans[a]);
    }
}

