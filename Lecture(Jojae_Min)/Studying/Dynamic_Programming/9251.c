//LCS(Longest Common Subsequence, 최장 공통 부분 수열)

#include <stdio.h>
#include <string.h>

int max(int a, int b){
    return a > b ? a : b;
}

int dp[1001][1001];

int main(){

    char a[1001], b[1001];

    scanf("%s", a);
    scanf("%s", b);

    int n = strlen(a);
    int m = strlen(b);

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(a[i-1] == b[j-1]){
                dp[i][j] = dp[i-1][j-1]+1;
            }
            else{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    printf("%d", dp[n][m]);

    return 0;
}


// int max(int a, int b){
//     return a > b ? a : b;
// }

// int dp[1001][1001];

// int main(){

//     char a[1001], b[1001];

//     scanf("%s", a);
//     scanf("%s", b);

//     int n = strlen(a);
//     int m = strlen(b);

//     if(a[0] == b[0]) dp[0][0] = 1;

//     for(int i = 1; i < m; i++){
//         if(a[0] == b[i]){
//             dp[0][i] = 1;
//         }
//         else{
//             dp[0][i] = max(dp[0][i], dp[0][i-1]);
//         }
//     }

//     for(int i = 1; i < n; i++){
//         if(a[i] == b[0]){
//             dp[i][0] = 1;
//         }
//         else{
//             dp[i][0] = max(dp[i][0], dp[i-1][0]);
//         }
//     }

//     for(int i = 1; i < n; i++){
//         for(int j = 1; j < m; j++){
//             if(a[i] == b[j]){
//                 dp[i][j] = dp[i-1][j-1]+1;
//             }
//             else{
//                 dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
//             }
//         }
//     }

//     printf("%d", dp[n-1][m-1]);

//     return 0;
// }

