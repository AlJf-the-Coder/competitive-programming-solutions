#include <stdio.h>
#include <set>

int main(){
    int n, s, m;
    int squares[200];
    scanf("%d %d %d", &n, &s, &m);
    for (int i = 0; i < n; i++)
        scanf("%d", squares + i);
    int ok = 1, curr = s;
    int k, hops = 0;
    std::set<int> past; 

    while (ok && squares[curr - 1] != m){
        past.insert(curr);
        k = squares[curr - 1];
        curr += k;
        ok = 1 <= curr && curr <= n && past.find(curr) == past.end();
        hops++;
    }

    if (ok)
        printf("magic\n");
    else if (curr < 1)
        printf("left\n");
    else if (curr > n)
        printf("right\n");
    else if (past.find(curr) != past.end())
        printf("cycle\n");
    
    printf("%d\n", hops);
}
