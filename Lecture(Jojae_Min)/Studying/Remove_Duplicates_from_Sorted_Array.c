#include <stdio.h>

// int removeDuplicates(int* nums, int numsSize) {
//     int count[201] = {};
//     for(int i = 0; i < numsSize; i++){
//         count[nums[i]+100]++;
//     }
    
//     int k = 0;
//     for(int i = 0; i < 201; i++){
//         if(count[i] != 0){
//             nums[k++] = i-100;
//         }

//     }
//     return k;
// }

// int removeDuplicates(int* nums, int numsSize) {
//     int left = 0;
//     int right = 1;
//     int k = 1;
//     for(int i = 1; i < numsSize; i++){
//         if(nums[left] == nums[right]){
//             right++;
//         }
//         else{
//             nums[k++] = nums[right];
//             left = right++;
//         }
//     }
//     return k;
// }

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    int k = 1;  // 다음에 넣을 위치

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[i - 1]) {
            nums[k++] = nums[i];
        }
    }

    return k;
}