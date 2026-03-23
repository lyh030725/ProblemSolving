#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}

int main(){

    int increse_dp[1000];
    int decrese_dp[1000];
    
    int n;
    scanf("%d", &n);

    int arr[1000] = {};

    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    for(int i = 0; i < n; i++){
        increse_dp[i] = 1;
        for(int j = 0; j < i; j++){
            if(arr[j] < arr[i]){
                increse_dp[i] = max(increse_dp[i], increse_dp[j]+1);
            }
        }
    }

    for(int i = n-1; i >=0 ; i--){
        decrese_dp[i] = 1;
        for(int j = n-1; j > i; j--){
            if(arr[j] < arr[i]){
                decrese_dp[i] = max(decrese_dp[i], decrese_dp[j]+1);
            }
        }
    }

    int max = 0;
    for(int i = 0; i < n; i++){
        int tmp = increse_dp[i] + decrese_dp[i];
        if(tmp > max) max = tmp;
    }

    printf("%d", max-1);

    return 0;
}