int max(int a, int b){
    return a > b ? a : b;
}

int robRange(int* nums, int start, int end){
    int n = end - start + 1;
    int dp[n];

    dp[0] = nums[start];
    if(n == 1) return dp[0];

    dp[1] = max(nums[start], nums[start+1]);

    for(int i = 2; i < n; i++){
        dp[i] = max(dp[i-1], dp[i-2] + nums[start + i]);
    }

    return dp[n-1];
}

int rob(int* nums, int numsSize) {
    if(numsSize == 1) return nums[0];

    int case1 = robRange(nums, 0, numsSize-2);
    int case2 = robRange(nums, 1, numsSize-1);

    return max(case1, case2);
}