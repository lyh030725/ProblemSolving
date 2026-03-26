//거스름돈

#include <stdio.h>

int main(){

    int n;
    scanf("%d", &n);

    int change = 1000-n;

    int res = 0;
    
    if(change >= 500){
        res += change/500;
        change %= 500;
    }
    if(change >= 100){
        res += change/100;
        change %= 100;
    }
    if(change >= 50){
        res += change/50;
        change %= 50;
    }
    if(change >= 10){
        res += change/10;
        change %= 10;
    }
    if(change >= 5){
        res += change/5;
        change %= 5;
    }
    res += change;

    printf("%d", res);

    return 0;
}