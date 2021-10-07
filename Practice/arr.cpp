#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> a(26);
    int i=0;
    int max=0;
    string let;
    cin >> let; // 문자 입력 완료
    transform(let.begin(), let.end(), let.begin(), ::toupper); // 모두 대문자로 변경
    while(let[i]){
        int temp = let[i];
        a[temp-65]++;
        i++; //나온 수만큼 배열에 정렬 0001003003000 이런식으로
    }
    for(auto N : a){ //N은 벡터 a의 원소 차례로
        if(max == N)
            max = -1; // 중복해서 등장했는지 filtering
        if(max < N)
            max = N; // 필터 이후에는 정상적인 max 탐색
    }
    if(max == -1)
        printf("?");
    else
        printf("%d", max);
}