int minCostClimbingStairs(int* cost, int costSize) {
    int dp[1001] = {cost[0], cost[1]};

    for(int i = 2; i <= costSize; i++){
        int a,b;
        if(i == costSize){
            a = dp[i-1];
            b = dp[i-2];
        }
        else{
            a = dp[i-1]+cost[i];
            b = dp[i-2]+cost[i];
        }
        if(a > b){
            dp[i] = b;
        }
        else{
            dp[i] = a;
        }
    }

    return dp[costSize];
}