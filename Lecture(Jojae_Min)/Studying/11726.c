// 2*n 타일링

#include <stdio.h>

int main(){
    int dp[1001] = {0,1,2};

    int n;
    scanf("%d", &n);

    if(n <= 2){
        printf("%d", dp[n]);
    }
    else{
        for(int i = 3; i <= n; i++){
            dp[i] = dp[i-1] + dp[i-2];
            dp[i] %= 10007;
        }
        printf("%d", dp[n]);
    }

    return 0;
}