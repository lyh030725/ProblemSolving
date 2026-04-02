//폴리오미노

#include <stdio.h>
#include <string.h>

int main(){

    char s[51] = {};
    char new_s[51] = {};

    scanf("%s", s);
    int n = strlen(s);

    int count = 0;
    int new_count = 0;

    for(int i = 0; i < n; i++){
        if(s[i] == 'X'){
            count++;
        }
        if(i == n-1 || s[i] == '.'){
            if(count % 2 == 1){
                printf("-1");
                return 0;
            }
            while(count >= 4){
                for(int j = 0; j < 4; j++){
                    new_s[new_count++] = 'A';
                }
                count -= 4;
            }
            if(count >= 2){
                for(int j = 0; j < 2; j++){
                new_s[new_count++] = 'B';
                }
            }
            if(s[i] == '.'){
                new_s[new_count++] = '.';
            }
            count = 0;
        }
    }

    printf("%s", new_s);


    return 0;
}