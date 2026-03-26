//파도반 수열

#include <stdio.h>

int main(){

    unsigned long long dp[100] = {1,1,1,2,2};

    int t;
    scanf("%d", &t);

    while(t--){
        unsigned long long n;
        scanf("%llu", &n);

        if(n <= 5){
        printf("%llu\n", dp[n-1]);
        }
        else{
            for(int i = 5; i < n; i++){
            dp[i] = dp[i-1] + dp[i-5];
            }
            printf("%llu\n", dp[n-1]);
        }
    }

    

    return 0;
}