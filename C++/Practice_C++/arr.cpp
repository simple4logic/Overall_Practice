#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> Ans;
    int min, max;
    scanf("%d %d", &min, &max);
    bool *test = new bool[max+1];

    //for(auto a : test) a=true; dynamic array does not support range-based loop
    for(int i=0;i<max+1;i++) //bool array init.
        test[i]=true;

    test[0]=false;
    test[1]=false; //about 0 & 1, make its decision not prime.

    for(long int i=2;i<=max+1;i++){
        if(test[i]){
            for(long int j =i*i; j<=max+1;j+=i){
                test[j]= false;
            }
        }
    }

    for(int k=2;k<min;k++)
        test[k]=false;

    //put values to Ans vector if it is true (=prime number)
    for(int j=0;j<max+1;j++){
        if(test[j])
            Ans.push_back(j);
    }
    for(auto b : Ans)
        printf("%d\n", b);

    delete []test;
 }