#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int countPrimes(int n){

    if(n <= 2) return 0;

    char* arr = (char*)malloc(sizeof(char)*n);

    for(int i = 0; i < n; i++){
        arr[i] = 1;
    }

    for(int i = 2; i*i < n; i++){
        if(arr[i]){
            for(int j = 2; i*j < n; j++){
                arr[i*j] = 0;
            }
        }
    }

    int count = 0;
    for(int i = 2; i < n; i++){
        if(arr[i]) count++;
    }

    free(arr);
    return count;
}


int main(){
    int n;

    scanf("%d", &n);
    printf("%d", countPrimes(n));

    return 0;
}