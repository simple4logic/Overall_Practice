#include <bits/stdc++.h>
using namespace std;

int main(){
    int min, max;
    scanf("%d %d", &min, &max);
    bool *test = new bool[max+1];

    //for(auto a : test) a=true; dynamic array does not support range-based loop
    for(int i=0;i<max+1;i++) //bool array init.
        test[i]=true;

    test[0]=false;
    test[1]=false; //about 0 & 1, make its decision not prime.

    for(int i=2;i<=max+1;i++){
        if(test[i]){
            if(i*i>1000001) break; //to prevent timeout (integer overflow)
            else{
                for(int j =i*i; j<=max+1;j+=i){ //look at here. if j starting with i*i, integer overflow occurs when i is over 46341.
                    test[j]= false;
                }
            }
        }
    }

    for(int k=2;k<min;k++) //make hint array false whose index is under min.
        test[k]=false;

    //print values if it is true (=prime number)
    for(int j=0;j<max+1;j++){
        if(test[j])
            printf("%d\n", j);
    }
}