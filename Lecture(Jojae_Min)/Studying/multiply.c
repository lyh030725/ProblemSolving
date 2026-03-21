#include <stdio.h>

int main(){
    unsigned long long a,b,c;
    scanf("%llu %llu %llu", &a, &b, &c);
    long long result = 1;
    while(b > 0){
        if(b%2 == 1){
            result *= a;
            result %= c;
            b--;
        }
        a *= a;
        a %= c;
        b /= 2;
    }
    printf("%llu", result);
    return 0;
}