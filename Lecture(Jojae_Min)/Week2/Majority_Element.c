#include <stdio.h>

int majorityElement(int* nums, int numsSize) {
    int cur = nums[0];
    int count = 1;
    for(int i = 1; i < numsSize; i++){
        if(cur != nums[i]){
            count--;
        }
        else{
            count++;
        }
        if(count == 0){
            cur = nums[i];
            count = 1;
        }
    }
    return cur;
}