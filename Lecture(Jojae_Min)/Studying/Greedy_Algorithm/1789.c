//수들의 합

#include <stdio.h>

int main(){

    unsigned long long s;
    scanf("%llu", &s);

    int cur = 1;
    int count = 0;
    while(s >= cur){
        count++;
        s-= cur++;
    }

    printf("%d", count);

    return 0;
}