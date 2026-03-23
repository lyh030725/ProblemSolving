//1로 만들기

#include <stdio.h>

int min(int a, int b){
    return a < b ? a : b;
}

int main(){

    int n;
    scanf("%d", &n);

    int start = 1;
    int dp[1000001] = {};
    for(int i = 2; i <= n; i++){
        dp[i] = 1000001;
    }
    dp[start] = 0;

    while(start != n){
        if(3*start <= n){
            dp[3*start] = min(dp[3*start], dp[start]+1);
        }
        if(2*start <= n){
            dp[2*start] = min(dp[2*start], dp[start]+1);
        }
        dp[start+1] = min(dp[start+1], dp[start]+1);
        start++;
    }

    printf("%d", dp[n]);



    return 0;
}