#include <bits/stdc++.h>
using namespace std;
set<int> prime;

void primegen(int N); //N is the even number that we're finding goldbach partition
void makeAns(int N); //same as primegen

int main(){
    int num;
    scanf("%d", &num);
    while(num--){
        int N;
        scanf("%d", &N);
        primegen(N); //generate prime number group under num
        makeAns(N);
    }
    
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
            prime.insert(k);
    }

    delete[] test;
}

void makeAns(int N){
    map<int, int> Ans;
    set<int> temp; //set for saving key, and finding minumum key.
    for(auto i : prime){ //repeat elements in prime group
        if(prime.count(N-i)){ //if i & N-i is both prime num, lets save it.
            if(i < (N-i)){
                Ans[(N-i)-i]=i; //when print, i & N-i
                temp.insert((N-i)-i);
            }
            else{
                Ans[i-(N-i)]=(N-i);
                temp.insert(i-(N-i));
            }
        }
        
    }
    int Answer = Ans[*temp.begin()];
    printf("%d %d", Answer, N-Answer);

    Ans.clear();
    temp.clear();
}