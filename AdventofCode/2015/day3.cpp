#include <bits/stdc++.h>
using namespace std;

void part1(){
    set <pair <int, int>> coords;
    pair <int, int> curr = make_pair(0, 0);
    coords.insert(curr);
    char c;
    while ((c = getchar()) != EOF){
        switch (c){
            case '^':
                curr.second += 1;
                coords.insert(curr);
                break;
            case 'v':
                curr.second -= 1;
                coords.insert(curr);
                break;
            case '>':
                curr.first += 1;
                coords.insert(curr);
                break;
            case '<':
                curr.first -= 1;
                coords.insert(curr);
                break;
        }
    }

    printf("%d\n", coords.size());
}

void part2(){
    set <pair <int, int>> coords_s;
    set <pair <int, int>> coords_r;
    pair <int, int> curr_s = make_pair(0, 0);
    pair <int, int> curr_r = make_pair(0, 0);
    coords_s.insert(curr_s);
    coords_r.insert(curr_r);
    bool santa = true;
    char c;

    while ((c = getchar()) != EOF){
        if (santa){
            switch (c){
                case '^':
                    curr_s.second += 1;
                    coords_s.insert(curr_s);
                    break;
                case 'v':
                    curr_s.second -= 1;
                    coords_s.insert(curr_s);
                    break;
                case '>':
                    curr_s.first += 1;
                    coords_s.insert(curr_s);
                    break;
                case '<':
                    curr_s.first -= 1;
                    coords_s.insert(curr_s);
                    break;
            }
        } else {
            switch (c){
                case '^':
                    curr_r.second += 1;
                    coords_r.insert(curr_r);
                    break;
                case 'v':
                    curr_r.second -= 1;
                    coords_r.insert(curr_r);
                    break;
                case '>':
                    curr_r.first += 1;
                    coords_r.insert(curr_r);
                    break;
                case '<':
                    curr_r.first -= 1;
                    coords_r.insert(curr_r);
                    break;
            }
        }
        santa = !santa;
    }


    int count = coords_s.size();
    for (auto it = coords_r.begin(); it != coords_r.end(); ++it){
        if (coords_s.find(*it) == coords_s.end())
            ++count;
    }

    printf("%d\n", count);
    
    // set <pair <int, int>> rs_union;
    // set_union(coords_r.begin(), coords_r.end(), coords_s.begin(), coords_s.end(), rs_union.begin()); 
    // printf("%d\n", rs_union.size());
}

int main(){
    // part1();
    part2();
}
