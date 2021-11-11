#include <bits/stdc++.h>
using namespace std;
vector<int> v;

void primegen(int N);

int main(){
    int num;
    scanf("%d", &num);
    primegen(num); //generate prime number group under num
    
}

void primegen(int N){
    bool *test = new bool[N+1];

    for(int i=0;i<N+1;i++) //bool array init.
        test[i]=true;

    test[0]=false;
    test[1]=false; //about 0 & 1, make its decision not prime.

    for(int i=2;i<=N+1;i++){
        if(test[i]){
            if(i*i>1000001) break; //to prevent timeout (integer overflow)
            else{
                for(int j =i*i; j<=N+1;j+=i){ //look at here. if j starting with i*i, integer overflow occurs when i is over 46341.
                    test[j]= false;
                } // j is the prime number.
            }
        }
    }

    for(int k=2;k<N+1;k++){
        if(test[k])
            v.push_back(k);
    }
}