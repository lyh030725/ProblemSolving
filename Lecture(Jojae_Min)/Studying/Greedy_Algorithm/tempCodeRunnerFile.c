//단어 수학

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    int x = ((int*)a)[0];
    int y = ((int*)b)[0];

    if(x < y) return 1;
    else if(x > y) return -1;
    else return 0;
}

int main(){

    int n;
    scanf("%d", &n);

    char data[10][9];
    int alpha_pos[10][26] = {};

    for(int i = 0; i < n; i++){
        scanf("%s", &data[i]);
        int m = strlen(data[i]);

        for(int j = 0; j < m; j++){
            alpha_pos[m-j][data[i][j]-'A']++;
        }        
    }

    int alpha_sum[26][2] = {};
    for(int i = 0; i < 26; i++){
        int count = 0;
        for(int j = 1; j < 10; j++){
            count = count*10 + alpha_pos[10-j][i];
        }
        alpha_sum[i][0] = count;
        alpha_sum[i][1] = i;
    }

    qsort(alpha_sum, 26, sizeof(alpha_sum[0]), compare);

    int alpha_weight[26] = {};
    for(int i = 0; i < 26; i++){
        // printf("%d %d\n", alpha_sum[i][0], alpha_sum[i][1]);
        alpha_weight[alpha_sum[i][1]] = 9-i;
    }

    // for(int i = 0; i < 26; i++){
    //     printf("%d\n", alpha_weight[i]);
    // }

    int result = 0;
    for(int i = 0; i < n; i++){
        int m = strlen(data[i]);
        int sum = 0;
        for(int j = 0; j < m; j++){
            sum = sum*10+alpha_weight[data[i][j]-'A'];
        }
        result += sum;
    }

    printf("%d", result);


    return 0;
}