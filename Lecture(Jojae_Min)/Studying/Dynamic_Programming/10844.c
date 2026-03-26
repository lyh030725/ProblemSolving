//쉬운 계단 수

#include <stdio.h>
#include <math.h>

int main(){
    int dp[100][10] = {{0,1,1,1,1,1,1,1,1,1}};

    int n;
    scanf("%d", &n);

    
    for(int i = 1; i < n; i++){
        for(int j = 0; j < 10; j++){
            if(j == 0){
                dp[i][j] = dp[i-1][1];
            }
            else if(j == 9){
                dp[i][j] = dp[i-1][8];
            }
            else{
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1];
            }
            dp[i][j] %= 1000000000;
        }
    }

    int result = 0;
    for(int i = 0; i < 10; i++){
        result += dp[n-1][i];
        result %= 1000000000;
    }

    printf("%d", result);


    return 0;
}