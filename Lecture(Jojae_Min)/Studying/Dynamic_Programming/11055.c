//가장 큰 증가하는 부분 수열

#include <stdio.h>

int max(int a, int b){
    return a > b ? a : b;
}


int main(){

    int dp[1000];

    int n;
    scanf("%d", &n);

    int data[1000];

    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
        dp[i] = data[i];
    }

    int max_val = data[0];

    for(int i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            if(data[i] > data[j]){
                dp[i] = max(dp[i], dp[j] + data[i]);
                max_val = max(max_val , dp[i]);
            }
        }
    }

    
    printf("%d", max_val);



    return 0;
}