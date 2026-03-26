//구간 합 구하기5

#include <stdio.h>

int sum[1025][1025];
int data[1024][1024];

int main(){
    int n,m;
    scanf("%d %d", &n, &m);
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            scanf("%d", &data[i][j]);
        }
    }

    sum[0][0] = data[0][0];
    for(int i = 1; i < n; i++){
        sum[0][i] = sum[0][i-1] + data[0][i];
        sum[i][0] = sum[i-1][0] + data[i][0];
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            sum[i][j] = sum[i-1][j] + sum[i][j-1] + data[i-1][j-1] - sum[i-1][j-1];
        }
    }

    for(int i = 0; i < m; i++){
        int x1,y1,x2,y2;
        scanf("%d %d", &x1, &y1);
        scanf("%d %d", &x2, &y2);
        int value = sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1];
        
        printf("%d\n", value);
    }

    return 0;


}