//주유소

#include <stdio.h>
#include <stdlib.h>

int main(){

    int n;
    scanf("%d", &n);

    unsigned long long dist[100000];
    unsigned long long price[100000];

    for(int i = 0; i < n-1; i++){
        scanf("%llu", &dist[i]);
    }

    for(int i = 0; i < n; i++){
        scanf("%llu", &price[i]);
    }

    unsigned long long cost = price[0]*dist[0];
    int start = 0;

    for(int i = 1; i < n-1; i++){
        if(price[start] > price[i]){
            start = i;
        }
        cost += price[start]*dist[i]; //can overflow
    }

    printf("%llu", cost);

    return 0;
}