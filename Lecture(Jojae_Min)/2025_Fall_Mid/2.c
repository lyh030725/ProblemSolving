//2.c

#include <stdio.h>

int main(){

    int n;
    scanf("%d", &n);

    int arr[2000] = {};
    int index[1000][2] = {};
    int length = 2*n;

    for(int i = 0; i < length; i++){
        scanf("%d", &arr[i]);
    }

    int count = 0;

    for(int i = 0; i < length; i++){
        for(int j = i+1; j < length; j++){
            if(arr[i] == arr[j]){
                index[arr[i]-1][0] = i;
                index[arr[i]-1][1] = j;
            }
        }
    }
    //{{0,2}, {1,4}, {2,5}}

    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            if(index[i][0] < index[j][0] && index[j][0] < index[i][1] && index[i][1] < index[j][1]
            || index[j][0] < index[i][0] && index[i][0] < index[j][1] && index[j][1] < index[i][1]){
                count++;
            }
        }
    }

    printf("%d", count);



    return 0;
}