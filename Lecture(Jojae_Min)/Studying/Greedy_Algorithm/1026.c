//보물

#include <stdio.h>
#include <stdlib.h>

int compare1(const void* a, const void* b){
    int x = *(int*)a;
    int y = *(int*)b;
    return x - y;
}

int compare2(const void* a, const void* b){
    int x = *(int*)a;
    int y = *(int*)b;
    return y-x;
}

int main(){

    int n;
    scanf("%d", &n);

    int arr1[50];
    int arr2[50];

    for(int i = 0; i < n; i++){
        scanf("%d", &arr1[i]);
    }
    for(int i = 0; i < n; i++){
        scanf("%d", &arr2[i]);
    }

    qsort(arr1, n, sizeof(int), compare1);
    qsort(arr2, n, sizeof(int), compare2);

    int sum = 0;
    for(int i = 0; i < n; i++){
        sum += arr1[i] * arr2[i];
    }

    printf("%d", sum);

    return 0;
}