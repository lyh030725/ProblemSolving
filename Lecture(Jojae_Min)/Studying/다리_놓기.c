#include <stdio.h>

unsigned long long fact(int n){
    unsigned long long result = 1;
    for(int i = 1; i <= n; i++){
        result *= i;
    }
    return result;
}

int main(){
    int t;
    scanf("%d", &t);

    for(int i = 0; i < t; i++){
        int n, m;
        scanf("%d %d", &n, &m);
        //mPn -> (m)!/(m-n)! // mCn -> mPn/n!
        unsigned long long result = 1;

        for(int j = 0; j < n; j++){
            result *= (m - j);
            result /= (j + 1);
        }

        printf("%llu\n", result);
    }
    return 0;
}