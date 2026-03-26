//신나는 함수 실행
#include <stdio.h>

int dp[21][21][21];

int main(){

    for(int i = 0; i < 21; i++){
        for(int j = 0; j < 21; j++){
            dp[i][j][0] = 1;
            dp[i][0][j] = 1;
            dp[0][i][j] = 1;
        }
    }

    for(int i = 1; i < 21; i++){
        for(int j = 1; j < 21; j++){
            for(int k = 1; k < 21; k++){
                if(i < j && j < k){
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k];
                }
                else{
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1];
                }
            }
        }
    }

    while(1){
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);

        if(a == -1 && b == -1 && c == -1){
            break;
        }
        if(a <= 0 || b <= 0 || c <= 0){
            printf("w(%d, %d, %d) = 1\n", a, b, c);
        }
        else{
            if(a > 20 || b > 20 || c > 20) printf("w(%d, %d, %d) = %d\n", a, b, c, dp[20][20][20]);
            else printf("w(%d, %d, %d) = %d\n", a, b, c, dp[a][b][c]);
        }

    }





    return 0;
}