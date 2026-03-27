//전자레인지

#include <stdio.h>

int main(){

    int a_count = 0;
    int b_count = 0;
    int c_count = 0;

    int t;
    scanf("%d", &t);

    if(t >= 300){
        a_count = t/300;
        t %= 300;
    }
    if(t >= 60){
        b_count = t/60;
        t %= 60;
    }
    if(t >= 10){
        c_count = t/10;
        t %= 10;
    }

    if(t == 0){
        printf("%d %d %d", a_count, b_count, c_count);
    }
    else{
        printf("-1");
    }


    return 0;
}