#include <stdio.h>

int singleNumber(int* nums, int numsSize) {
    int count[60001] = {};
    for(int i = 0; i < numsSize; i++){
        count[nums[i]+30000]++;
    }
    int result;

    for(int i = 0; i <= 60000; i++){
        if(count[i] == 1){
            result = i - 30000;
        }
    }
    
    return result;
}

// int singleNumber(int* nums, int numsSize) {
//     int result = 0;

//     for(int i = 0; i < numsSize; i++){
//         result ^= nums[i];
//     }

//     return result;
// }


int main(){
    int nums[5] = {4,1,2,1,2};

    printf("%d" , singleNumber(nums, 5));

    return 0;
}