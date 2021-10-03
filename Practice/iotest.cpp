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

long long sum(std::vector<int> &a) {
	long long ans = 0;
    int i=0;
    int n =a.size();
    while(n--){
        ans+=a[i];
        i++;
    }
	return ans;
}

