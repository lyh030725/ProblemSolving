//뒤집기

#include <stdio.h>
#include <string.h>

int main(){

    char s[1000000];

    scanf("%s", s);

    int is_zero = 0;
    if(s[0] == '0') is_zero = 1;

    int count = 0;
    int one_count = 0;
    int zero_count = 0;
    int n = strlen(s);

    for(int i = 1; i < n; i++){
        if(is_zero){
            if(s[i] == '1'){
                zero_count++;
                is_zero = 0;
            }
        }
        else{
            if(s[i] == '0'){
                one_count++;
                is_zero = 1;
            }
        }
    }

    if(is_zero) zero_count++;
    else one_count++;

    if(zero_count > one_count) printf("%d", one_count);
    else printf("%d", zero_count);



    return 0;
}