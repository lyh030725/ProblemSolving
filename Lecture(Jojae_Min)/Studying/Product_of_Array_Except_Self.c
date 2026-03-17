#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize) {

    int product1[100000] = {1, nums[0], };
    int product2[100000] = {1, nums[numsSize-1], };

    for(int i = 2; i < numsSize; i++){
        product1[i] = product1[i-1]*nums[i-1];
    }

    for(int i = 0; i < 4; i++){
        printf("%d ", product1[i]);
    }
    printf("\n");
    for(int i = 2; i < numsSize; i++){
        product2[i] = product2[i-1]*nums[numsSize-i];
    }

    for(int i = 0; i < 4; i++){
        printf("%d ", product2[i]);
    }
    printf("\n");

    int* answer = (int*)malloc(sizeof(int)*numsSize);

    for(int i = 0; i < numsSize; i++){
        answer[i] = product1[i]*product2[numsSize-1-i];
    }

    return answer;
}


int main(){
    int nums[] = {1,2,3,4};
    int* answer;

    answer = productExceptSelf(nums, 4);

    for(int i = 0; i < 4; i++){
        printf("%d ", answer[i]);
    }

    return 0;
}