//1.c

#include <stdio.h>

int max(int a, int b){
    return a < b ? b : a;
}

int main(){

    int arr[3][3] = {};

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            scanf("%d", &arr[i][j]);
        }
    }


    int corner_max = max(max(max(arr[0][0], arr[0][2]), arr[2][0]), arr[2][2]);

    int flag = 1;

    if(arr[0][1] <= corner_max) flag = 0; 
    if(arr[2][1] <= corner_max) flag = 0; 
    for(int j = 0; j < 3; j++){
        if(arr[1][j] <= corner_max){
            flag = 0;
            break;
        }
    }

    if(flag){
        printf("plus");
    }
    else{
        printf("none");
    }



    return 0;
}