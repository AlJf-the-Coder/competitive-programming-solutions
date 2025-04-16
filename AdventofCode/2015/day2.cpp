#include <bits/stdc++.h>
using namespace std;

void part1(){
    int l, w, h, extra, add, total = 0;
    char c;
    while ((c = getchar()) != EOF){
        ungetc(c, stdin);
        scanf("%d%*c%d%*c%d%*c", &l, &w, &h);

        add = l * w;
        total += 2 * add;
        extra = add; 

        add = l * h;
        total += 2 * add;
        extra = min(extra, add);

        add = w * h;
        total += 2 * add;
        extra = min(extra, add);

        total += extra;
    }
    printf("%d\n", total);
}

void part2(){
    int total = 0;
    char c;
    int dim[3];
    while ((c = getchar()) != EOF){
        ungetc(c, stdin);
        scanf("%d%*c%d%*c%d%*c", &dim[0], &dim[1], &dim[2]);

        int g = 0; //index of max
        for (int i = 1; i < 3; ++i)
            if (dim[i] > dim[g])
                g = i;

        for (int i = 0; i < 3; ++i)
            if (i != g)
                total += 2 * dim[i];

        total += dim[0] * dim[1] * dim[2];

    }
    printf("%d\n", total);
}

int main(){
    part1();
    part2();
    return 0;
}
