//피보나치 함수

#include <stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    int zero[41] = {1};
    int one[41] = {0, 1};

    for(int i = 2; i <= 40; i++){
            zero[i] = zero[i-1] + zero[i-2];
            one[i] = one[i-1] + one[i-2];
        }

    while(t--){
        int n;
        scanf("%d", &n);
        printf("%d %d\n", zero[n], one[n]);
    }

    return 0;
}