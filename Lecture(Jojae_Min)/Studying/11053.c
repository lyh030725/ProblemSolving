//가장 긴 증가하는 부분 수열

#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}

int main(){

    int n;
    scanf("%d", &n);

    int data[1000];
    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }

    int dp[1000];

    for(int i = 0; i < n; i++){
        dp[i] = 1;
    }

    for(int i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            if(data[i] > data[j]){
                dp[i] = max(dp[i], dp[j]+1);
            }
        }
    }

    int result = 1;

    for(int i = 0; i < n; i++){
        result = max(result, dp[i]);
    }

    printf("%d", result);

    return 0;
}