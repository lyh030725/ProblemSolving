//정수 삼각형
#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}

int main(){

    int data[500][500] = {};

    int n;
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        for(int j = 0; j < i+1; j++){
            scanf("%d", &data[i][j]);
        }
    }

    int dp[500][500] = {{data[0][0]}};

    for(int i = 0; i < n-1; i++){
        for(int j = 0; j < i+1; j++){
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+data[i+1][j]);
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+data[i+1][j+1]);
        }
    }

    int result = 0;
    for(int i = 0; i < n; i++){
        result = max(result, dp[n-1][i]);
    }

    printf("%d", result);


    return 0;
}