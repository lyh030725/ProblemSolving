//수리공 항승

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    int x = *(int*)a;
    int y = *(int*)b;

    if(x < y) return -1;
    else if(x > y) return 1;
    else return 0;
}

int main(){
    
    int n, l;

    scanf("%d %d", &n, &l);

    int data[1000];

    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }

    qsort(data, n, sizeof(int), compare);

    int check[1001] = {};
    // int result = 0;

    // for(int i = 0; i < n; i++){
    //     if(check[data[i]] == 0){
    //         check[data[i]] = 1;
    //         result++;
    //         for(int j = i+1; j < n; j++){
    //             if(data[j]-data[i]+1 <= l){
    //                 check[data[j]] = 1;
    //             }
    //         }
    //     }
    // }

    int result = 1;
    int pos = data[0];
    for(int i = 1; i < n; i++){
        if(data[i] > pos+l-1){
            pos = data[i];
            result++;
        }
    }

    printf("%d", result);


    return 0;
}