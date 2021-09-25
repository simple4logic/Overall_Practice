#include<iostream>
using namespace std;

int arr[27] = {3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 };

int Alp(char a){
    for(int i=0;i<26;i++){
        if(a==i+65)
            return arr[i];
    }
    return 0;
}

int main(){
    char a[2001];
    char b[2001];
    cin.getline(a,2001,'\n');
    cin.getline(b,2001,EOF); //파일 끝까지 입력받기

    char* allarr = alptonum(a, b); //allarr에 모든 숫자 기록
}

int alptonum(char* a, char* b){ //배열 두개 입력하면 번갈아가면서 숫자로 바꿔주는 함수
    int arr[4002];
    int i=0;
    while(a[i++]=='\0'){
        arr[2*i]=Alp(a[i]);
        arr[2*i+1]=Alp(b[i]);
    }
    return arr;
}


int sum(char* a){ //모든 숫자가 기록된 배열 a, 앞에 두개씩 더하면 됨
    if (arrlen(a)<3)
        printf("%d%d", a[]) //@@@@@@@@@@@@@@@@@@@@@@@@@@@!!!
    
    int arr[2001];
    while(a[i++]=='\0'){
        arr[i]=(a[2*i]+a[2*i+1]);
    }
    return 
}

/*
sum(char *a)
새로운 arr
return sum(새로운 arr)

if arrlen <3
return %1d, %1d
*/