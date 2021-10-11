#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    vector<int> A, B;
    for(;a;){ //until A<1
        A.push_back(a%10); //맨 끝자리 삽입
        B.push_back(b%10);
        a /= 10; // 맨끝자리 삭제
        b /= 10;
    }
    int x = 0, y = 0;
    for (auto a : A)
        x = x*10 + a;
    for (auto a : B)
        y = y*10 + a;
    printf("%d", max(x, y));
}