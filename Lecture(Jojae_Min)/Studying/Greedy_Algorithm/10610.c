//30

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b){
    int x = *(int*)a;
    int y = *(int*)b;
    if(x < y) return 1;
    else if(x > y) return -1;
    else return 0;
}

int main(){

    //10^5 O(nlong)
    char s[100001];
    scanf("%s", s);
    int n = strlen(s);

    int nums[100001];
    int sum = 0;

    for(int i = 0; i < n; i++){
        nums[i] = s[i] - '0';
        sum += nums[i];
    }


    qsort(nums, n, sizeof(int), compare);

    if(nums[n-1] != 0 || sum % 3 != 0){
        printf("-1");
        return 0;
    }

    for(int i = 0; i < n; i++){
        printf("%d", nums[i]);
    }



    return 0;
}