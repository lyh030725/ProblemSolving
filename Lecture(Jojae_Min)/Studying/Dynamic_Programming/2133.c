//타일 채우기

#include <stdio.h>

int main(){

    int dp[31] = {1,0,3,0,11};

    int n;

    scanf("%d", &n);

    for(int i = 5; i <= 30; i++){
        dp[i] = dp[i-2]*3;
        if(i%2==0){
            for(int j = 0; j <= i-4; j += 2){
                dp[i] += dp[j]*2;
            }
        }
    }

    printf("%d", dp[n]);


    return 0;
}