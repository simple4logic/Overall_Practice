#include<iostream>
using namespace std;

int main(){
    char str[101];

    while(cin.getline(str, 101, '\n')){
        cout << str << endl;
    }
}