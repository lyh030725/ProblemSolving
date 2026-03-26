//동전 1

#include <stdio.h>

// int dp[101][10001];

// int max(int a, int b){
//     return a > b ? a : b;
// }

// int max3(int a, int b){
//     return a > b ? a : b;
// }

// int main(){

//     int n, k;
    
//     scanf("%d %d", &n, &k);

//     int data[100];

//     for(int i = 0; i < n; i++){
//         scanf("%d", &data[i]);
//     }

//     for(int i = 1; i <= n; i++){
//         for(int j = 1; j <= k; j++){
//             int count = j/data[i-1];
//             int sum = 0;
//             if(j % data[i-1] == 0) sum = 1;   
//             for(int k = 0; k <= count; k++){
//                 if(dp[i-1][j-k*data[i-1]] == 0){
//                     continue;
//                 }
//                 sum += dp[i-1][j-k*data[i-1]];
//             }
//             dp[i][j] = max(dp[i-1][j], sum);
//         }
//     }

//     // for(int i = 0; i <= n; i++){
//     //     for(int j = 0; j <=k; j++){
//     //         printf("%d ", dp[i][j]);
//     //     }
//     //     printf("\n");
//     // }

//     printf("%d", dp[n][k]);




//     return 0;
// }

#include <stdio.h>

int dp[10001];

int main(){
    int n, k;
    scanf("%d %d", &n, &k);

    int coin[100];

    for(int i = 0; i < n; i++){
        scanf("%d", &coin[i]);
    }

    dp[0] = 1; // 핵심 초기값

    for(int i = 0; i < n; i++){
        for(int j = coin[i]; j <= k; j++){
            dp[j] += dp[j - coin[i]];
        }
    }

    printf("%d", dp[k]);
    return 0;
}