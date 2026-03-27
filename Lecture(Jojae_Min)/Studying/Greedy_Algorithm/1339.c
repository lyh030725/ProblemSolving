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

// #include <stdio.h>
// #include <string.h>
// #include <stdlib.h>

// long long weight[26];
// int is_first[26];

// int compare(const void* a, const void* b){
//     long long x = *(long long*)a;
//     long long y = *(long long*)b;
//     if(x < y) return 1;
//     else if(x > y) return -1;
//     return 0;
// }

// int main(){
//     int n;
//     scanf("%d", &n);

//     char s[10];

//     for(int i = 0; i < n; i++){
//         scanf("%s", s);
//         int len = strlen(s);

//         is_first[s[0]-'A'] = 1;

//         long long p = 1;
//         for(int j = len-1; j >= 0; j--){
//             weight[s[j]-'A'] += p;
//             p *= 10;
//         }
//     }

//     // 0 줄 문자 찾기
//     int zero_idx = -1;
//     long long min_val = 1e18;

//     for(int i = 0; i < 26; i++){
//         if(!is_first[i] && weight[i] > 0){
//             if(weight[i] < min_val){
//                 min_val = weight[i];
//                 zero_idx = i;
//             }
//         }
//     }

//     // weight 배열 복사해서 정렬용 만들기
//     long long temp[26];
//     for(int i = 0; i < 26; i++) temp[i] = weight[i];

//     qsort(temp, 26, sizeof(long long), compare);

//     int digit[26] = {0};
//     int used[26] = {0};

//     int num = 9;

//     for(int i = 0; i < 26; i++){
//         if(temp[i] == 0) break;

//         // zero로 쓸 애는 건너뜀
//         if(temp[i] == min_val){
//             digit[zero_idx] = 0;
//             used[zero_idx] = 1;
//             continue;
//         }

//         // 실제 알파벳 찾기
//         for(int j = 0; j < 26; j++){
//             if(!used[j] && weight[j] == temp[i]){
//                 digit[j] = num--;
//                 used[j] = 1;
//                 break;
//             }
//         }
//     }

//     // 결과 계산
//     long long result = 0;

//     // 다시 입력 받아 계산 (또는 저장해둬도 됨)
//     rewind(stdin);

//     scanf("%d", &n);
//     for(int i = 0; i < n; i++){
//         scanf("%s", s);
//         long long val = 0;
//         for(int j = 0; s[j]; j++){
//             val = val*10 + digit[s[j]-'A'];
//         }
//         result += val;
//     }

//     printf("%lld", result);

//     return 0;
// }