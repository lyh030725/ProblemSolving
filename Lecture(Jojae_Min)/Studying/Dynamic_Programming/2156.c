//포도주 시식

#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}

int max3(int a, int b, int c){
    return max(max(a, b), c);
}

int main(){

    int data[10000] = {};

    int n;
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }

    if(n == 1){
        printf("%d", data[0]);
    }
    else if(n == 2){
        printf("%d", data[0]+data[1]);
    }
    else if(n==3){
        printf("%d", max3(data[0]+data[2], data[1]+data[2], data[0]+data[1]));
    }
    else{
        int dp[10000] = {data[0], data[0]+data[1], max3(data[0]+data[2], data[1]+data[2], data[0]+data[1])};

        for(int i = 3; i < n; i++){
            dp[i] = max3(dp[i-3]+data[i-1]+data[i], dp[i-2]+data[i], dp[i-1]);
        }

        // int result = 0;
        // for(int i = 0; i < n; i++){
        //     result = max(result, dp[i]);
        // }

        printf("%d", dp[n-1]);
    }
    
    return 0;
}