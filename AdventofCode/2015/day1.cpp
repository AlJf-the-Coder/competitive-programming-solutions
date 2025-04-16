#include <bits/stdc++.h>
using namespace std;

void part1(){
    char c = getchar();
    int floor = 0;
    while (c != EOF){
        switch (c){
            case '(':
                ++floor;
                break;
            case ')':
                --floor;
        }
        c = getchar();
    }
    printf("%d\n", floor);
}

void part2(){
    char c = getchar();
    int floor = 0;
    int pos = 1;
    while (c != EOF){
        switch (c){
            case '(':
                ++floor;
                break;
            case ')':
                --floor;
        }
        if (floor == -1){
            break;
        }
        c = getchar();
        ++pos;
    }
    printf("%d %d\n", floor, pos);
}

int main(){
    part1();
    part2();
}
