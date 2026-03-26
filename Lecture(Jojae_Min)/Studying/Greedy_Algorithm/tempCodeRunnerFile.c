//회의실 배정

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    int* x = (int*)a;
    int* y = (int*)b;
    if(x[1] < y[1]) return -1;
    else if(x[1] > y[1]) return 1;
    else return x[0] - y[0];
}

int main(){

    int n;
    scanf("%d", &n);

    int data[100000][2];

    for(int i = 0; i < n; i++){
        scanf("%d %d", &data[i][0], &data[i][1]);
    }

    for(int i = 0; i < n; i++){
        printf("%d %d\n", &data[i][0], &data[i][1]);
    }

    int res = 1;
    int end = data[0][1];
    for(int i = 1; i < n; i++){
        if(data[i][0] >= end){
            end = data[i][1];
            res++;
        }
    }


    printf("%d", res);


    return 0;
}