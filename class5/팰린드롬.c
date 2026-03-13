#include <stdio.h>

int dp[2001][2001];
int data[2001];

int main(){
    int n;
    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        scanf("%d", &data[i]);
    }

    // 길이 1
    for(int i = 1; i <= n; i++){
        dp[i][i] = 1;
    }

    // 길이 2
    for(int i = 1; i < n; i++){
        if(data[i] == data[i+1]){
            dp[i][i+1] = 1;
        }
    }

    // 길이 3 이상
    for(int len = 3; len <= n; len++){
        for(int i = 1; i <= n - len + 1; i++){
            int j = i + len - 1;

            if(data[i] == data[j] && dp[i+1][j-1]){
                dp[i][j] = 1;
            }
        }
    }

    int m;
    scanf("%d", &m);

    while(m--){
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\n", dp[a][b]);
    }

    return 0;
}
