// int max_(int a, int b){
//     return a > b ? a : b;
// }

// int max(int a, int b, int c){
//     return max_(max_(a,b), c);
// }

// int rob(int* nums, int numsSize) {
//     if(numsSize == 1) return nums[0];
//     if(numsSize == 2) return max_(nums[0], nums[1]);
//     if(numsSize == 3) return max_(nums[0]+nums[2], nums[1]);

//     int dp[100] = {nums[0], nums[1], max_(nums[0]+nums[2], nums[1])};

//     for(int i = 3; i < numsSize; i++){
//         dp[i] = max(dp[i-1], dp[i-2]+nums[i], dp[i-3]+nums[i]);
//     }

//     return dp[numsSize-1];

// }

int max(int a, int b){
    return a > b ? a : b;
}

int rob(int* nums, int numsSize) {
    if(numsSize == 1) return nums[0];
    if(numsSize == 2) return max(nums[0], nums[1]);

    int dp[100] = {nums[0], max(nums[0], nums[1])};

    for(int i = 2; i < numsSize; i++){
        dp[i] = max(dp[i-1], dp[i-2]+nums[i]);
    }

    return dp[numsSize-1];

}