//신입 사원

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    int* x = (int*)a;
    int* y = (int*)b;

    return x[0] - y[0];
}

int main(){

    int t;
    scanf("%d", &t);

    while(t--){
        int n;
        scanf("%d", &n);

        int arr[100000][2] = {};
        for(int i = 0; i < n; i ++){
            scanf("%d %d", &arr[i][0], &arr[i][1]);
        }

        qsort(arr, n, sizeof(arr[0]), compare);

        int count = 1;
        int min = arr[0][1];    
        for(int i = 0; i < n; i++){
            if(arr[i][1] < min){
                min = arr[i][1];
                count++;
            }
        }
        
        printf("%d\n", count);
    }
    //(1,4), (2,5), (3,6), (4,2), (5,7), (6,1), (7,3)
    //(1,4), (2,3), (3,2), (4,1), (5,5)
    //(1,2), (2,1)

    return 0;
}