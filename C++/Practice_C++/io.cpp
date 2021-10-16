#include <bits/stdc++.h>
using namespace std;

int main(){
    int goal, speed, fail, now_h =0, day=1;
    scanf("%d %d %d",&speed, &fail,&goal);
    printf("%d", (goal-speed)/(speed-fail));
}
/*
    높이가 V 미터인 나무를 올라감
    하루에 A미터씩 올라감
    밤에 B미터씩 미끄러짐

    골 = 10
*/