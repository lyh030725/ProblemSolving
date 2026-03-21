#include <stdio.h>

int main(){
    unsigned long long s;
    scanf("%llu", &s);
    
    unsigned long long sum = 1;
    unsigned long long n = 1;
    while(1){
        if(sum == s) break;
        if(sum > s){
            n--;
            break;
        }
        n++;
        sum += n;
    }
    printf("%llu", n);

    return 0;
}