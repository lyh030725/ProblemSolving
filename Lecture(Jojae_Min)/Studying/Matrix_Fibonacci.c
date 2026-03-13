#include <stdio.h>

void multiply(long long A[2][2], long long B[2][2]) {
    long long temp[2][2];

    temp[0][0] = (A[0][0]*B[0][0] + A[0][1]*B[1][0])%1000000;
    temp[0][1] = (A[0][0]*B[0][1] + A[0][1]*B[1][1])%1000000;
    temp[1][0] = (A[1][0]*B[0][0] + A[1][1]*B[1][0])%1000000;
    temp[1][1] = (A[1][0]*B[0][1]+ A[1][1]*B[1][1])%1000000;

    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++)
            A[i][j] = temp[i][j];
}

void power(long long A[2][2], long long n) {
    long long base[2][2] = {{1,1},{1,0}};

    while(n > 0) {
        if(n % 2 == 1)
            multiply(A, base);

        multiply(base, base);
        n /= 2;
    }
}

long long fibonacci(long long n) {
    if(n == 0) return 0;

    long long result[2][2] = {{1,0},{0,1}}; // 단위행렬
    power(result, n-1);

    return result[0][0];
}

int main() {
    long long n;
    scanf("%lld", &n);

    printf("%lld\n", fibonacci(n));

    return 0;
}
