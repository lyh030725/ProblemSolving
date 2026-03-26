//카드 구매하기

#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}

int main(){

    int n;
    scanf("%d", &n);

    int dp[1001] = {};

    int data[1001] = {};

    for(int i = 1; i <= n; i++){
        scanf("%d", &data[i]);
    }
    
    // for(int i = 1; i <= n; i++){
    //     for(int j = i; j <= n; j++){
    //         int count = j/i;
    //         for(int k = 0; k <= count; k++){
    //             dp[j] = max(dp[j], k*data[i] + dp[j-k*i]);
    //         }
    //         // printf("%d ", dp[j]);
    //     }
    //     // printf("\n");
    // }

    for(int i = 1; i <= n; i++){
        for(int j = i; j <= n; j++){
            dp[j] = max(dp[j], data[i] + dp[j-i]);
            // printf("%d ", dp[j]);
        }
        // printf("\n");
    }

    printf("%d", dp[n]);

    return 0;
}