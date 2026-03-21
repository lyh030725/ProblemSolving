#include <stdio.h>

// void moveZeroes(int* nums, int numsSize) {
//     int index = 0;
//     int new_nums[numsSize];
//     for(int i = 0; i < numsSize; i++){
//         if(nums[i] != 0){
//             new_nums[index++] = nums[i];
//         }
//     }
//     for(int i = index; i < numsSize; i++){
        
//         new_nums[i] = 0;
//     }

//     for(int i = 0; i < numsSize; i++){
//         nums[i] = new_nums[i];
//     }
// }

void moveZeroes(int* nums, int numsSize) {
    int index = 0;

    for(int i = 0; i < numsSize; i++){
        if(nums[i] != 0){
            int temp = nums[index];
            nums[index] = nums[i];
            nums[i] = temp;
            index++;
        }
    }
}

int main(){
    int nums[5] = {0,1,0,3,12};

    moveZeroes(nums, 5);

    for(int i = 0; i < 5; i++){
        printf("%d ", nums[i]);
    }

    return 0;
}