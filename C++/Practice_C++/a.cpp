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

    for(int i=2;i<=max+1;i++){
        if(test[i]){
            if(i*i>1000001) break;
            else{
                for(long int j =i*i; j<=max+1;j+=i){
                    test[j]= false;
                }
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


 /*
 처음 arr 를 f(=0) f(=1) 나머지 (2부터 소수맞음)true로 초기화 해놓는다.
 2부터 n+1까지 i를 loop
 배열 값이 true라면(소수라면) 정답 배열에 append한다.
 그 다음 for loop 시작 2*i 부터 n+1 까지 i만큼 이동 (처음에는 i=2이므로 2배수이동.)
 2배수 모두 false

//바로 앞에꺼가 지워놓은 다음에도 여전히 true인 다음 숫자들은 소수가 맞다 n의 배수까지 지운다음 살아남은 n+1은 당연히 소수이다. 
 i=3일 경우 loop는 
 3은 아직 살아남아서 ansarr에 append... 반복

/바로 앞에꺼가 지워놓은 다음에도 여전히 true인 다음 숫자들은 소수가 맞다 n의 배수까지 지운다음 살아남은 n+1은 당연히 소수이다. 
 i=3일 경우 loop는 
 3은 아직 살아남아서 ansarr에 append... 반복

 그런데 이중 루프의 시작인 i*2는 i*i로 개선할 수 있다. i*k(1<=k<=i-1)까지는 이전 소수 배수들이 이미 다 밀어버렸기 때문

 */