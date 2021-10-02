#include<iostream>
#include<vector>
using namespace std;
long long sum(int* a, int n);
int main(){
    int x,n=0; // n = 입력받은 정수 개수
    vector<int> arr(0);
    while(~scanf("%d", &x)){
        arr.push_back(x);
        n++;
    }
    int* b = new int[n+1];
    copy(arr.begin(), arr.end(), b);
    printf("%lld", sum(b, n));
}
long long sum(int*a, int n){
    long long Ans=0;
    int i=0;
    while(n--){
        Ans+=a[i];
        i++;
    }
    return Ans;
}
