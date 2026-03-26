//계단 오리기

#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}

int main(){

    int stairs[301] = {};

    int n;
    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        scanf("%d", &stairs[i]);
    }

    int dp[301] = {0,stairs[1], stairs[1]+stairs[2]};
    
    if(n <= 2){
        printf("%d", dp[n]);
    }
    else{
        for(int i = 3; i <= n; i++){
            dp[i] = max(dp[i-3]+stairs[i-1], dp[i-2]) + stairs[i];
        }
        printf("%d", dp[n]);
    }

    return 0;
}