#include <stdio.h>
#include <math.h>
#include <limits.h>

int dp[100001];
int main(){
    int n;
    scanf("%d", &n);

    for(int n = 1; n*n <= 100000; n++){
        dp[n*n] = 1;
    }

    for(int i = 2; i <= n; i++){
        if(dp[i] == 1) continue;
        dp[i] = INT_MAX;
        for(int j = 1; j*j < i; j++){
            int tmp = dp[j*j] + dp[i-(j*j)];
            if(tmp < dp[i]){
                dp[i] = tmp;
            }
        }
    }
    printf("%d", dp[n]);

    
    return 0;
}