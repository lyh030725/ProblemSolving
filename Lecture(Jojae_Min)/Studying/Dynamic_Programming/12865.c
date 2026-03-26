//평범한 배낭

#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}

int dp[101][100001];

int main(){
    int n, k;
    scanf("%d %d", &n, &k);

    int w[101];
    int v[101];

    for(int i = 1; i <= n; i++){
        scanf("%d %d", &w[i], &v[i]);
    }

    

    for(int i = 1; i <= n; i ++){
        for(int j = 0; j <= k; j++){
            if(j >= w[i]){
                dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j]);
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }

    printf("%d", dp[n][k]);

    return 0;
}