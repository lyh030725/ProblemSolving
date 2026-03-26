//01 타일

#include <stdio.h>

int dp[1000000];

int main(){

    dp[0] = 1;
    dp[1] = 2;

    int n;
    scanf("%d", &n);

    for(int i = 2; i < n; i++){
        dp[i] = dp[i-1] + dp[i-2];
        dp[i] %= 15746;
    }

    printf("%d", dp[n-1]);

    return 0;
}