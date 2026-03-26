//RGB거리

#include <stdio.h>
#include <limits.h>

int min(int a, int b){
    return a < b ? a : b;
}

int min3(int a, int b, int c){
    return min(min(a,b), c);
}

int main(){

    int n;
    scanf("%d", &n);

    int data[1000][3];

    for(int i = 0; i < n; i++){
        scanf("%d %d %d", &data[i][0], &data[i][1], &data[i][2]);
    }

    int dp[1000][3] = {{data[0][0], data[0][1], data[0][2]}};

    for(int i = 1; i < n; i++){
        dp[i][0] = INT_MAX;
        dp[i][1] = INT_MAX;
        dp[i][2] = INT_MAX;
        dp[i][0] = min3(dp[i][0], dp[i-1][1]+data[i][0], dp[i-1][2]+data[i][0]);
        dp[i][1] = min3(dp[i][1], dp[i-1][0]+data[i][1], dp[i-1][2]+data[i][1]);
        dp[i][2] = min3(dp[i][2], dp[i-1][0]+data[i][2], dp[i-1][1]+data[i][2]);
    }

    printf("%d", min3(dp[n-1][0], dp[n-1][1], dp[n-1][2]));
    return 0;
}