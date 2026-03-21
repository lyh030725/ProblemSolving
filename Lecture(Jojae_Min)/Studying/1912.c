//연속합
#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}

int main(){

    int n;

    scanf("%d", &n);


    int data[100000];

    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }

    int dp[100000] = {data[0]};

    for(int i = 1; i < n; i++){
        dp[i] = max(data[i], dp[i-1]+data[i]);
    }

    int result = data[0];

    for(int i = 0; i < n; i++){
        result = max(result, dp[i]);
    }

    printf("%d\n", result);


    return 0;
}