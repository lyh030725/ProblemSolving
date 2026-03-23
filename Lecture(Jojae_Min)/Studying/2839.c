//설탕 배달
#include <stdio.h>

int min(int a, int b){
    return a < b ? a : b;
}

int main(){
    int n;
    scanf("%d", &n);

    int dp[1001] = {};

    int length = n/5;
    for(int i = 0; i <= length; i++){
        int copy_n = n;
        copy_n -= 5*i;
        if(copy_n % 3 == 0){
            dp[i] = i + copy_n/3;
        }
        else{
            dp[i] = 5001;
        }
    }

    int result = 5001;
    for(int i = 0; i <= length; i++){
        result = min(result, dp[i]);
    }

    if(result == 5001){
        printf("-1");
    }
    else{
        printf("%d", result);
    }

    return 0;
}