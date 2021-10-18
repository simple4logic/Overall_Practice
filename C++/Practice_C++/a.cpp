#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> Ans;
    int min, max;
    scanf("%d %d", &min, &max);
    int arr[2]={max, min};
    bool *test = new bool[max+1];

    for(auto a : test) a=true; 
    test[0]=false;
    test[1]=false; //bool array 초기화
    
    for(auto x : arr){
        for(int i=2;i<=x+1;i++){
            if(test[i]){
                //Ans.push_back(i); //어짜피 삽입은 test 배열 기반으로 나중에 한꺼번에 하면 됨.
                for(int j =i*i;j*j<=x+1;j++){
                    test[j]= ~test[j]; //default : false; //비트 반전
                }
            }
        }
    }
    int i=0;
    for(auto y : test){
        if(test[i])
            Ans.push_back(i);
        i++;
    }
    for(auto b : Ans)
        printf("%d\n", b);
 }


 /*
 처음 arr 를 f(=0) f(=1) 나머지 (2부터 소수마즘)true로 초기화 해놓는다.
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