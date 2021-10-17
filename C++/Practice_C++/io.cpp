#include <bits/stdc++.h>
using namespace std;

int main(){
    int goal, speed, fail, now_h =0, day=1;
    scanf("%d %d %d",&speed, &fail, &goal);
    printf("%d", (int)ceil((double)(goal-speed)/(double)(speed - fail))+1);
}
