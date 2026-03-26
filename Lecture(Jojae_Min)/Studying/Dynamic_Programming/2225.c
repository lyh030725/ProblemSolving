//합분해

#include <stdio.h>

int dp[201][201];

int main(){

    for(int i = 0; i <= 200; i++){
        dp[i][0] = 1;
    }
    
    int n,k;

    scanf("%d %d", &n, &k);

    for(int i = 1; i <= k; i++){
        for(int j = 1; j <= n; j++){
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
            dp[i][j] %= 1000000000;
        }
    }

    printf("%d", dp[k][n]);


    return 0;
}