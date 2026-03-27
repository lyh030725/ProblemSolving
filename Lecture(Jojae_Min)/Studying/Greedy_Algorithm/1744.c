//수 묶기

#include <stdio.h>

int main(){

    int count[2001] = {};
    int n;

    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        int num;
        scanf("%d", &num);
        count[num+1000]++;
    }

    int sum = 0;
    int cur_count = 0;
    int cur = 0;

    for(int i = 0; i <= 1000; i++){
        if(count[i] == 0) continue;
        if(cur_count == 0){
            cur_count = count[i];
            cur = i - 1000;
            if(cur_count > 1){
                for(int i = 0; i < cur_count/2; i++){
                    sum += cur*cur;
                }
                cur_count %= 2;
            }
        }
        else{
            if(cur_count >= count[i]){
                sum += cur*(i-1000)*count[i];
                cur_count -= count[i];
            }
            else{
                sum += cur*(i-1000)*cur_count;
                cur_count = count[i]-cur_count;
                cur = i - 1000;
            }
        }
    }
    for(int i = 0; i < cur_count; i++){
        sum += cur;
    }

    cur_count = 0;
    cur = 0;
    for(int i = 2000; i > 1001; i--){
        if(count[i] == 0) continue;
        if(cur_count == 0){
            cur_count = count[i];
            cur = i - 1000;
            if(cur_count > 1){
                for(int i = 0; i < cur_count/2; i++){
                    sum += cur*cur;
                }
                cur_count %= 2;
            }
        }
        else{
            if(cur_count >= count[i]){
                sum += cur*(i-1000)*count[i];
                cur_count -= count[i];
            }
            else{
                sum += cur*(i-1000)*cur_count;
                cur_count = count[i]-cur_count;
                cur = i - 1000;
            }
        }
    }

    for(int i = 0; i < cur_count; i++){
        sum += cur;
    }
    for(int i = 0; i < count[1001]; i++){
        sum += 1;
    }

    printf("%d", sum);

    return 0;
}


// #include <stdio.h>

// int main(){
//     int count[2001] = {0};
//     int n;

//     scanf("%d", &n);

//     for(int i = 0; i < n; i++){
//         int x;
//         scanf("%d", &x);
//         count[x + 1000]++;
//     }

//     int sum = 0;

//     // 🔥 1은 그냥 더하기
//     sum += count[1001];

//     // 🔥 음수 + 0 (작은 것부터)
//     int prev = -1001; // 아직 없음
//     int hasPrev = 0;

//     for(int i = 0; i <= 1000; i++){
//         while(count[i]--){
//             int cur = i - 1000;

//             if(!hasPrev){
//                 prev = cur;
//                 hasPrev = 1;
//             }
//             else{
//                 sum += prev * cur;
//                 hasPrev = 0;
//             }
//         }
//     }

//     // 남은 음수 처리
//     if(hasPrev){
//         sum += prev;
//     }

//     // 🔥 양수 (2 이상, 큰 것부터)
//     hasPrev = 0;

//     for(int i = 2000; i >= 1002; i--){
//         while(count[i]--){
//             int cur = i - 1000;

//             if(!hasPrev){
//                 prev = cur;
//                 hasPrev = 1;
//             }
//             else{
//                 sum += prev * cur;
//                 hasPrev = 0;
//             }
//         }
//     }

//     // 남은 양수 처리
//     if(hasPrev){
//         sum += prev;
//     }

//     printf("%d", sum);
//     return 0;
// }