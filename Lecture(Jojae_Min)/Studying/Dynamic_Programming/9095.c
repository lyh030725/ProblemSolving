//1,2,3 더하기

#include <stdio.h>

int main(){

    int t;
    scanf("%d", &t);

    while(t--){
        int n;
        scanf("%d", &n);
        int dp[11] = {0,1,2,4};
        if(n <= 3){
            printf("%d\n", dp[n]);
        }
        else{
            for(int i = 4; i <= n; i++){
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
            }
            printf("%d\n", dp[n]);
        }
    }

    return 0;
}