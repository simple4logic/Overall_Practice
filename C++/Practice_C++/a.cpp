#include <bits/stdc++.h>
using namespace std;

int main(){
    int num, maxVal; //maxVal is the result value that we should reach by adding three elements
    scanf("%d %d", &num, &maxVal);
    int* arr = new int[num];
    int cnt = num;
    while(cnt--){
        int t;
        scanf("%d", &t);
        arr[cnt]=t;
    }

    int max=0,sum=0; //current max. when it reaches maxVal, stop loop and return maxVal.

    for(int i=0;i<num-2;i++){ //i should be below length-2
        for(int j=i+1;j<num-1;j++){ // j should be below length-1
            for(int k=j+1;k<num;k++){
                sum=(arr[i]+arr[j]+arr[k]);
                if((max < sum)&&(sum<=maxVal))
                    max = sum;
                if(max == maxVal){
                    printf("%d", maxVal);
                    return 0;
                }
            }
        }
    }

    printf("%d", max);
}