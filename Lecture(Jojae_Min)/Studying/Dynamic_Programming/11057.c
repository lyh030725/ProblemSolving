//오르막 수

#include <stdio.h>

int dp[1001][10];

int main(){

    for(int i = 0; i < 10; i++) dp[1][i] = 1;

    int n;
    scanf("%d", &n);

    // for(int i = 2; i <= n; i++){
    //     for(int j = 0; j < 10; j++){
    //         for(int k = j; k < 10; k++){
    //             dp[i][j] += dp[i-1][k];
    //             dp[i][j] %= 10007;
    //         }
    //     }
    // }

    for(int i = 2; i <= n; i++){
        for(int j = 0; j < 10; j++){
            if(j == 0)
                dp[i][j] = dp[i-1][j];
            else
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007;
        }
    }
    
    int result = 0;

    for(int i = 0; i < 10; i++){
        // printf("%d ", dp[n][i]);
        result += dp[n][i];
        result %= 10007;
    }

    printf("%d", result);

    return 0;
}