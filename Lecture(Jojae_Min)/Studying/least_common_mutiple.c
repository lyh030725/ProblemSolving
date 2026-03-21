#include <stdio.h>

int gcd(int a, int b){
    if(b > a){
        int temp = a;
        a = b;
        b = temp;
    }
    // 10 6 = 4
    while(b != 0){
        int r = a % b;
        a = b; // a = 6 // a = 4 // a = 2
        b = r; // b = 4 // b= 2 // b = 0
    }
    return a;
}

int main(){
    int t;
    scanf("%d", &t);

    while(t--){
        int a,b;
        scanf("%d %d", &a, &b);
        int result = (a*b)/gcd(a,b);
        printf("%d\n", result);
    }
    return 0;
}