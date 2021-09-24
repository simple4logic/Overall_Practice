#include<iostream>
using namespace std;

int day(int a);

int main(){
    int x, y;
    cin >> x >> y;

    if(x==2){
       day((31+y)%7);
    }
    /*다음 월에 따른 날짜 합산 필요*/
}

int day(int a){
    if(a == 0)
        printf("MON");
    else if(a== 1)
        printf("TUE");
    else if(a ==2)
        printf("WED");
    else if(a==3)
        printf("THU");
    else if(a==4)
        printf("FRI");
    else if(a==5)
        printf("SAT");
    else
        printf("SUN");
    return 0;
}

/*
x =2 이고 y =1 이면 
2월 1일 = 32일
31일 더한것

+31

+7하면 같은 요일이다.
*/