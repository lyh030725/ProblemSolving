//돌 게임

// #include <stdio.h>

// char dp[1001];

// int main(){

//     int n;

//     scanf("%d", &n);
//     dp[0] = 'C';

//     for(int i = 0; i <= n; i++){
//         if(dp[i] == 'S'){
//             if(dp[i+1] == 0){
//                 dp[i+1] = 'C';
//             }
//             if(dp[i+3] ==  0){
//                 dp[i+3] = 'C';
//             }
//         }
//         else{
//             if(dp[i+1] == 0){
//                 dp[i+1] = 'S';
//             }
//             if(dp[i+3] ==  0){
//                 dp[i+3] = 'S';
//             }
//         }
//     }

//     if(dp[n] == 'S') printf("SK");
//     else printf("CY");



//     return 0;
// }

#include <stdio.h>

int dp[1001];

int main(){

    int n;
    scanf("%d", &n);

    dp[1] = 1;
    dp[2] = 0;
    dp[3] = 1;

    for(int i = 4; i <= n; i++){
        if(dp[i-1] == 0 || dp[i-3] == 0){
            dp[i] = 1;
        }
        else{
            dp[i] = 0;
        }
    }

    if(dp[n]) printf("SK");
    else printf("CY");
    
    return 0;
}