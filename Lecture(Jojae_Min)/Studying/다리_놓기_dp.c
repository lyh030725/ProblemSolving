#include <stdio.h>

unsigned long long dp[31][31];

int main(){
    for(int i = 0; i <= 30; i++){
        for(int j = 0; j <= i; j++){
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

        printf("%llu\n", dp[m][n]);
        

    }

    return 0;
}