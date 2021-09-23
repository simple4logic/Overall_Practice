# Q11719

## Input
입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄이 주어질 수도 있고, 각 줄의 앞 뒤에 공백이 있을 수도 있다.

## Output
입력받은 그대로 출력한다.

## 예제 입력
```
    Hello

Baekjoon     
   Online Judge    
```

## 예제 출력

```
    Hello

Baekjoon     
   Online Judge    
```

## 나의 제출
```
#include<iostream>
using namespace std;

int main(){
    char str[101]; // 100글자 이하의 입력받을 한 줄

    while(cin.getline(str, 101, '\n')){ 
        // 공백이 올 때까지 입력받음. 입력받지 못하면 false return.

        cout << str << endl; // 매번 입력받고 개행하고 loop
    }
}
```

## 총평

while 조건문 안에 대입문을 넣어서 처리해서 깔금한 코드를 쓸 수 있었다. 기분 아주 만족스러움.