//내리막 길

#include <stdio.h>

int m,n;
int graph[500][500];
long long dp[500][500];

int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

long long dfs(int x, int y){
    if(x == m-1 && y == n-1) return 1;

    if(dp[x][y] != -1) return dp[x][y];

    dp[x][y] = 0;

    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(0 <= nx && nx < m && 0 <= ny && ny < n){
            if(graph[x][y] > graph[nx][ny]){
                dp[x][y] += dfs(nx, ny);
            }
        }
    }

    return dp[x][y];
}

int main(){
    scanf("%d %d", &m, &n);

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            scanf("%d", &graph[i][j]);
            dp[i][j] = -1; // 중요
        }
    }

    printf("%lld", dfs(0,0));
}