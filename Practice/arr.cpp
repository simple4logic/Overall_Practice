#include <iostream>
using namespace std;

int main(){
    int n,a,x;
    double sum=0;
    cin>>n; //테스트 케이스의 수
    while(n--){
        int cnt=0;
        cin >> a;
        int* cls = new int[a+1];
        while(a--){
            cin >> cls[a+1];
            sum+=cls[a+1];
        } // 첫번째 케이스 입력 다받고 점수 합계 구함
        for(int i=0;i<sizeof(cls)/4;i++){
            if(cls[i]>(sum/sizeof(cls)/4))
                printf("!!!\n");
                //cnt++;
        }
        printf("%.3lf%%\n", cnt/a*100);

        delete[] cls;
    }
}