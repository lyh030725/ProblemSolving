//카드 정렬하기

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

    int card[100000];

    for(int i = 0; i < n; i++){
        scanf("%d", &card[i]);
    }

    qsort(card, n, sizeof(int), compare);

    return 0;
}