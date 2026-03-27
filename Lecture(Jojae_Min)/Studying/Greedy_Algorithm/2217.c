//로프

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    int x = *(int*)a;
    int y = *(int*)b;

    return x-y;
}

int main(){

    int n;
    scanf("%d", &n);

    int data[100000];

    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }

    qsort(data, n, sizeof(int), compare);

    int max = 0;

    for(int i = 0; i < n; i++){
        int tmp = data[i]*(n-i);
        if(tmp > max) max = tmp;
    }

    printf("%d", max);


    return 0;
}