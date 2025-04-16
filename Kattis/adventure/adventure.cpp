#include <stdio.h>

int main(){
    int n;
    scanf("%d%*c", &n);
    char backpack[102];
    for (int i = 0; i < n; i++){
        int top = -1;
        int pass = 1;
        char c = getchar();
        while (pass && c != '\n' && c != EOF){
            switch (c){
                case '.':
                    break;
                case '$':
                    top++;
                    backpack[top] = c;
                    break;
                case '*':
                    top++;
                    backpack[top] = c;
                    break;
                case '|':
                    top++;
                    backpack[top] = c;
                    break;
                case 'b':
                    if (top > -1 && backpack[top] == '$')
                        top--;
                    else
                        pass = 0;
                    break;
                case 'j':
                    if (top > -1 && backpack[top] == '*')
                        top--;
                    else
                        pass = 0;
                    break;
                case 't':
                    if (top > -1 && backpack[top] == '|')
                        top--;
                    else
                        pass = 0;
                    break;
            }
            c = getchar();
        }

        if (c != '\n' && c != EOF)
           fgets(backpack, 102, stdin); 

        if (pass && top = -1)
            printf("YES\n");
        else
            printf("NO\n");
    }

    return 0;
}
