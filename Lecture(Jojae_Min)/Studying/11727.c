//2*n 타일링 2

#include <stdio.h>
    
int main(){

    int dp[1000] = {1, 3};

    int n;
    scanf("%d", &n);

    for(int i = 2; i < n; i++){
        dp[i] = dp[i-1]+2*dp[i-2];
        dp[i] %= 10007;
    }

    printf("%d", dp[n-1]);


    return 0;
}