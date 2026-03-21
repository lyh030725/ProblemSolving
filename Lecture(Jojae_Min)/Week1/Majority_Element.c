#include <stdio.h>

int majorityElement(int* nums, int numsSize) {
    int cur = nums[0];
    int cur_count = 1;
    for(int i = 1; i < numsSize; i++){
        if(cur_count == 0){
            cur = nums[i];
            cur_count = 1;
            continue;
        }
        if(cur != nums[i]){
            cur_count--;
        }
        else{
            cur_count++;
        }
    }
    return cur;
}

int main(){
    
}