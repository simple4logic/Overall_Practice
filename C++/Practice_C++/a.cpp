#include <bits/stdc++.h>
using namespace std;

class point{
    private:
        int x;
        int y;
    public:
        point(int input_x, int input_y){
            x = input_x;
            y = input_y;
        }
        void pX(){ const
            return x;
        }
        void pY(){ const
            return y;
        }

};

double dist(point a1, point a2);
int sol(double dist, int r1, int r2);

int main(){
    int n;
    scanf("%d", &n);
    while(n--){
            int x1, y1, r1, x2, y2, r2;
            scanf("%d %d %d %d %d %d", x1, y1, r1, x2, y2, r2);
        }
    }
}

double dist(point a1, point a2){
    double X = pow((a1.pX()-a2.pX()), 2);
    double Y = pow((a1.pY()-a2.pY()), 2);
    double Z = sqrt(X+Y);
    return Z;
}

int sol(double dist, int r1, int r2){
    if(dist < (r1+r2))
        return 2;
    else if(dist > (r1+r2))
        return 0;
    else return 1; //when dist = radius1 & 2
}