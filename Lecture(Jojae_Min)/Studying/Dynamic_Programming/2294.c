//동전 2

#include <stdio.h>

#define MAX 10001

int dp[10001] = {};

int min(int a, int b){
    return a < b ? a : b;
}

int main(){
    int n, k;

    scanf("%d %d", &n, &k);

    int coin[100];

    for(int i = 0; i < n; i++){
        scanf("%d", &coin[i]);
    }

    for(int i = 1; i <= k; i++){
        dp[i] = MAX;
    }

    for(int i = 0; i < n; i++){
        for(int j = coin[i]; j <= k; j++){
            dp[j] = min(dp[j], dp[j-coin[i]] + 1);
            // printf("%d ", dp[j]);
        }
        // printf("\n");
    }

    if(dp[k] == MAX){
        printf("-1");
    }
    else{
        printf("%d", dp[k]);
    }
    
    return 0;

}