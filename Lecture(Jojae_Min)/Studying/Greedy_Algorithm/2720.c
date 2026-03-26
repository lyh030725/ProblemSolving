//세탁소 사장 동혁

#include <stdio.h>

int main(){

    int t;
    scanf("%d", &t);

    while(t--){
        int q_num = 0;
        int d_num = 0;
        int n_num = 0;
        int p_num = 0;

        int num;
        scanf("%d", &num);

        if(num >= 25){
            q_num = num/25;
            num %= 25;
        }
        if(num >= 10){
            d_num = num/10;
            num %= 10;
        }
        if(num >= 5){
            n_num = num/5;
            num %= 5;
        }
        p_num = num;

        printf("%d %d %d %d\n", q_num, d_num, n_num, p_num);
    }



    return 0;
}