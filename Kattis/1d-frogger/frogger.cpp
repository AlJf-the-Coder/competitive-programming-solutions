#include <stdio.h>

int main(){
    int n, s, m;
    int squares[200];
    scanf("%d %d %d", &n, &s, &m);
    for (int i = 0; i < s; i++)
        scanf("%d", squares + i);
    int ok = curr = 1;
    int k, hops = 0;
    
    while (ok && squares[curr - 1] != m){
        k = squares[curr - 1];
        curr += k;
        // also test if looping
        ok = 1 <= curr && curr <= s;
        hops++;
    }

    if (ok)
        printf("magic\n");
    else if (curr < 1)
        printf("left\n");
    else if (curr > s)
        printf("left\n");
    else if (same)
        printf("cycle\n");
    
    printf("%d\n", hops);
}
