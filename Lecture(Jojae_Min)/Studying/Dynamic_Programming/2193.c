//이친수

#include <stdio.h>

int main(){

    unsigned long long zero[91] = {0,0};
    unsigned long long  one[91] = {0,1};

    int n;
    scanf("%d", &n);

    for(int i = 2; i <= n; i++){
        zero[i] = zero[i-1]+one[i-1];
        one[i] = zero[i-1];
    }

    printf("%llu", zero[n]+one[n]);

    return 0;
}