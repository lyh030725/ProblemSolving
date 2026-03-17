#include <stdio.h>

int gcd(int a, int b){
    if(a < b){
        int tmp = a;
        a = b;
        b = tmp;
    }
    int r = 0;
    while(b>0){
        r = a%b;
        a = b;
        b = r;
    }
    return a;
}

int main(){
    int a,b,c,d;
    scanf("%d %d", &a, &b);
    scanf("%d %d", &c, &d);
    int result_deno = (b*d)/gcd(b,d);
    int result_nom = d/gcd(b,d)*a + b/gcd(b,d)*c;
    int gcd_ = gcd(result_deno, result_nom);
    
    result_deno /= gcd_;
    result_nom /= gcd_;

    printf("%d %d", result_nom, result_deno);

    return 0;
}