#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int arr[100000];

    for(int i = 0; i < n; i++){
        int input_num;
        scanf("%d", &input_num);
        arr[i] = input_num;
    }

    long long cur = arr[0];
    long long max = arr[0];

    for(int i = 1; i < n; i++){
        if(cur < 0){
            cur = arr[i];
        }
        else{
            cur += arr[i];
        }
        if(cur > max) max = cur;
    }
    printf("%lld", max);
    return 0;
}