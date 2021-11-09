#include <bits/stdc++.h>

class Point{
    public:
        int x;
        int y;
       
        Point(int input_x, int input_y){
            x = input_x;
            y = input_y;
        }
        
};

double dist(Point a1, Point a2);
int sol(double dist, int r1, int r2);

int main(){
    int n;
    scanf("%d", &n);
    while(n--){
            int x1, y1, r1, x2, y2, r2;
            scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
            Point p1(x1, y1);
            Point p2(x2, y2);
            double D = dist(p1, p2);
            int Ans = sol(D, r1, r2);
            printf("%d\n", Ans);
        }
}

double dist(Point a1, Point a2){
    double X = pow((a1.x-a2.x), 2);
    double Y = pow((a1.y-a2.y), 2);
    double Z = sqrt(X+Y);
    return Z;
}

int sol(double dist, int r1, int r2){
    if(dist == 0)
        return 0;

    if(dist < (r1+r2))
        return 2;
    else if(dist > (r1+r2))
        return 0;
    else return 1; //when dist = radius1 & 2
}