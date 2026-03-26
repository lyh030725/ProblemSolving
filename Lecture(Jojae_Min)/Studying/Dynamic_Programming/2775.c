//부녀회장이 될거야

#include <stdio.h>


int main(){

    int t;
    scanf("%d", &t);

    int dp[15][15] = {};
    for(int i = 0; i < 15; i++){
        dp[0][i] = i;
    }

    for(int i = 1; i < 15; i++){
        for(int j = 1; j < 15; j++){
            for(int k = 1; k <= j; k++){
                dp[i][j] += dp[i-1][k];
            }
        }
    }

    while(t--){
        int k,n;
        scanf("%d", &k);
        scanf("%d", &n);
        printf("%d\n", dp[k][n]);
    }

    return 0;
}