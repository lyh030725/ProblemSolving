#include <stdio.h>
#include <string.h>

int main(){

    char num[100001];
    int num_index[10] = {};

    scanf("%s", num);

    int length = strlen(num);
    for(int i = 1; i < length; i++){
        int int_num = num[i]-'0';
        if(i > num_index[int_num]){
            num_index[int_num] = i;
        }
    }


    for(int i = 0; i < length; i++){
        int int_num = num[i]-'0';
        int flag = 0;
        for(int j = 9; j > int_num; j--){
            if(num_index[j] > i){
                char temp = num[i];
                num[i] = num[num_index[j]];
                num[num_index[j]] = temp;
                flag = 1;
                break;
            }
        }
        if(flag) break;
    }

    int leading_zero = 0;
    while(leading_zero < length && num[leading_zero] == '0'){
        leading_zero++;
    }

    if(leading_zero == length){
        printf("0");
    }
    else{
        for(int i = leading_zero; i < length; i++){
        printf("%c", num[i]);
        }
    }
    

    return 0;
}