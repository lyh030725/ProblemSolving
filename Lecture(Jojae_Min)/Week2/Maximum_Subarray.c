#include <stdio.h>


int maxSubArray(int* nums, int numsSize) {
    int max = nums[0];
    int cur = nums[0];

    for(int i = 1; i < numsSize; i++){
        if(cur < 0) cur = nums[i];
        else cur += nums[i];

        if(cur > max) max = cur;
    }

    return max;
}
int main(){
    int nums[] = {-5, -6, -7, -8, -9, -1};
    printf("%d", maxSubArray(nums, 6));
    return 0;
}