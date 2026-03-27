// A -> B

#include <stdio.h>

int main(){

    int a, b;
    scanf("%d %d", &a, &b);

    int count = 1;

    while(b > a){
        if(b % 2 == 0){
            b /= 2;
        }
        else if(b % 10 == 1){
            b /= 10;
        }
        else{
            printf("-1");
            return 0;
        }
        count++;
    }

    if(a == b) printf("%d", count);
    else printf("-1");

    return 0;
}