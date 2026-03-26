//동전 0

#include <stdio.h>

int main(){

    int n,k;

    scanf("%d %d", &n, &k);

    int data[10];
    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }

    int res = 0;

    for(int i = n-1; i >= 0; i--){
        if(k >= data[i]){
            res += k/data[i];
            k %= data[i];
        }
    }

    printf("%d", res);


    return 0;
}