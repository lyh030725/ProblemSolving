//다리 놓기

#include <stdio.h>

int main(){
    int dp[31][31] = {};
    for(int i = 0; i < 31; i++){
        for(int j = 0; j < 31; j++){
            if(j == 0 || j == i){
                dp[i][j] = 1;
                continue;
            }
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
        }
    }

    int t;
    scanf("%d", &t);

    while(t--){
        int n,m;
        scanf("%d %d", &n, &m);

        printf("%d\n", dp[m][n]);
    }



    return 0;
}