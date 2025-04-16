#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>



int sum_fib_even(int n){
    // get sum of all even fibonacci numbers less than fib(n)
    int fib_arr[n+1];
    fib_arr[0] = fib_arr[1] = 1;
    int sum = 0;
    for (int i=2; i<n+1; i++){
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2];
    }
    for (int i=2; i<n+1; i = i + 3){
        sum = sum + fib_arr[i];
    }
    return sum;
}

int fib_lim(int bound){
    // find value lowest value of n such that fib(n) is not less than bound
    int fib_minus_2 = 1;
    int fib_minus_1 = 1;
    int fib_curr = fib_minus_2 + fib_minus_1;
    int sum = 0;
    int i;
    for (i=2; ; i++){
        if (fib_curr < bound){
            fib_minus_2 = fib_minus_1;
            fib_minus_1 = fib_curr;
            fib_curr = fib_minus_1 + fib_minus_2;
        }
        else{
            printf("%d\n", fib_curr);
            break;
        }
    }
    return i;
}

int fib(int n){
    //calculate fib using closed formula}
    double sqrt_5 = sqrt((double) 5);
    return (int)(((5+sqrt_5)/10)*pow((1 + sqrt_5)/2,n) + ((5-sqrt_5)/10)*pow((1 - sqrt_5)/2,n)); 
}

int sum_3_or_5(int n){
    int sum_k(int k){
        int divByK = (n-1)/k;
        divByK = k * divByK * (divByK+1)/2.0;
        return divByK;
    }
    int sum = 0;
    if (n == 0) return sum; 
    return sum_k(3) + sum_k(5) - sum_k(15);
}

long long largest_prime_factor(long long n){
    long long limit = sqrt(n);
    for (long long i=2 ; i <= limit; i++){
            if (n % i == 0){
                return largest_prime_factor(n/i);
            }
    }
    return n;
}

long long largest_prime_factor2(long long n){
    long long limit = sqrt(n);
    for (long long i=2 ; i <= limit; i++){
            while (n % i == 0 && i <= limit){
                n = n/i;
                limit = sqrt(n);

            }
    }
    return n;
}

int is_prime(int n){
    int limit = sqrt(n);
    if (n % 2 == 0) return 0;
    for (int i=3 ; i <= limit; i = i+2){
            if (n % i == 0){
                return 0;
            }
    }
    return 1;
}
int string_to_int(char str[]){
    //make integer from string from lowest place digit to biggest
    int place = 1;
    int len = strlen(str);
    int ret = 0;
    for (int i = 1; i<len+1; i++){
        ret = ret + ((int) str[len-i] - 48) * place;
        place = place * 10;
    }
    return ret;
}

void int_to_string(int num, char str[], int arr_len){
    int len = 1;
    int factor = 1;
    while (num / (factor * 10) > 0 ){
        len = len + 1;
        factor = factor * 10;
    }

    int min = (arr_len - 1 > len) ? len: arr_len - 1;
    for (int i = 0; i < min; i++){
        str[i] = num / factor + 48;
        num = num % factor;
        factor = factor/10;
    }
    str[min] = '\0';
}

int is_palindrome(char str[]){
    int len = strlen(str);
    int mid = (len-1)/2;
    for (int i = 0; i <=mid; i++ ){
        if (str[i] != str[len-1-i]){
            return 0;
        }
    }
    return 1;
}

int largest_palindrome_product(int d){
    char prod[2*d + 1];
    int big = pow(10, d) - 1;
    int small = pow(10, d-1);
    int max = -1;
    int factors[2];
    for (int i = big; i> small - 1; i--){
        for (int j = i; j>small - 1; j--){
            int_to_string(i * j, prod, 2*d + 1);
            if (is_palindrome(prod)){
                if (i*j > max){
                    max = i*j;
                    factors[0] = i;
                    factors[1] = j;
                }
                
            }
        }
    }
    printf("%d x %d\n", factors[0], factors[1]);
    return max;
}
void lengthen_array(int **arr, int size){
    int * new_arr = malloc(size*2);
    memcpy(new_arr, *arr, size);
    free(*arr);
    *arr = new_arr;
}
int num_divisible(int n, int d){
    int div = 0;
    while (n % d == 0){
        div++;
        n = n/d;
    }
    return div;
}

int * prime_array(int n){
    //creates array of primes 1st element is number of primes in array
    int *primes = malloc(5 * sizeof(int));
    int size = 5 * sizeof(int);
    primes[1] = 2;
    int ind = 2;
    for (int i = 3; i<=n; i= i+2){
        if (is_prime(i)) {
            primes[ind] = i;
            ind++;
        }
        if (ind * sizeof(int) == size){ 
            lengthen_array(&primes, size);
            size = size * 2;
        }
    }
    primes[0]= ind - 1;
    return primes;
}

int * counts_array(int n){
    int * primes = prime_array(n);
    int length = primes[0] + 1;
    int * counts = malloc(length*sizeof(int));

    for (int i = 1; i < length; i++){
        counts[i] = 1;
    }

    for (int i = 4; i <= n; i++){
        if (is_prime(i)) continue;
        int num = i;
        for (int j = 1; j < length; j++){
            int prime = primes[j];
            int count = 0;
            if (num < prime) {
                break;
            }
            while (num%prime == 0){
                count++;
                num = num/prime;
            }
            if (count > counts[j]){
                counts[j] = count;
            }    
        }
    }
    for (int j = 1; j < length; j++){
            printf("%d %d\n", primes[j], counts[j]);
        }
    printf("\n");
    free(primes);
    return counts; 
}

int smallest_evenly_divisible(int range){
    int *primes = prime_array(range);
    int *counts = counts_array(range);
    int ret = 1;
    for (int i= 1; i<= primes[0]; i++){
        ret = ret * pow(primes[i], counts[i]);
    }
    free(primes);
    free(counts);
    return ret;
}
int sum_square_diff(int n){
    return ((3*n + 2)*(pow(n, 3) - n))/12;
}

int nth_prime(int n){
    int count = 1;
    int i = 1;
    if (n == 1) return 2;
    while (count != n){
        i = i +2;
        if (is_prime(i)) count++;
    }
    return i;
}

long long largest_adjacent_product(int n){
    char huge_int[1001];
    char *ints = malloc(n+1);
    ints[n] = '\0';
    for (int i = 0; i < 20; i++){
        fgets(huge_int + 50*i, 1001, stdin);
    }
    huge_int[1000] = 0;
    long long max = 0;
    for (int i = 0; i< 1000 - n + 1; i++){
        long long prod = 1;
        for (int j = 0; j < n; j++){
            if (huge_int[i+j] == '0'){
                i = i + j;
                prod = 1;
                break;
            }
            prod = prod * (huge_int[i+j] - 48);
        }
        if (prod > max){
            max = prod;
            memcpy(ints, huge_int+i, n);
        }
    }
    printf("%s\n", ints);
    free(ints);
    return max;
}

int pythagorean_triplets(int n){
    int a,b,c;
    for (int a = 1; a<n; a++){
        for (int b = a; b<n; b++){
            c = sqrt(pow(a, 2)+pow(b,2));
            if ((pow(c,2) == pow(a, 2)+pow(b,2)) && (a + b + c == n)){
                printf("%d %d %d\n", a, b, c);
                return a*b*c;
            }
        }
    }
    return -1;
}

int main(void){
    int n = 1000;
    printf("max product is %d\n", pythagorean_triplets(n));
    return 0;
}