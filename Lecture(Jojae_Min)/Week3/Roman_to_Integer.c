#include <string.h>

// int romanToInt(char* s) {
//     int length = strlen(s);
//     int res = 0;
//     for(int i = 0; i < length; i++){
//         if(s[i] == 'I'){
//             if(i == length-1){
//                 res += 1;
//             }
//             else{
//                 if(s[i+1] == 'V'){
//                     res += 4;
//                     i++;
//                 }
//                 else if(s[i+1] == 'X'){
//                     res += 9;
//                     i++;
//                 }
//                 else{
//                     res += 1;
//                 }
//             }
//         }
//         else if(s[i] == 'X'){
//             if(i == length-1){
//                 res += 10;
//             }
//             else{
//                 if(s[i+1] == 'L'){
//                     res += 40;
//                     i++;
//                 }
//                 else if(s[i+1] == 'C'){
//                     res += 90;
//                     i++;
//                 }
//                 else{
//                     res += 10;
//                 }
//             }
//         }
//         else if(s[i] == 'C'){
//             if(i == length-1){
//                 res += 100;
//             }
//             else{
//                 if(s[i+1] == 'D'){
//                     res += 400;
//                     i++;
//                 }
//                 else if(s[i+1] == 'M'){
//                     res += 900;
//                     i++;
//                 }
//                 else{
//                     res += 100;
//                 }
//             }
//         }
//         else if(s[i] == 'V'){
//             res += 5;
//         }
//         else if(s[i] == 'L'){
//             res += 50;
//         }
//         else if(s[i] == 'D'){
//             res += 500;
//         }
//         else{
//             res += 1000;
//         }
//     }
//     return res;
// }

int value(char c){
    if(c=='I') return 1;
    if(c=='V') return 5;
    if(c=='X') return 10;
    if(c=='L') return 50;
    if(c=='C') return 100;
    if(c=='D') return 500;
    return 1000;
}

int romanToInt(char* s) {
    int res = 0;
    int n = strlen(s);

    for(int i = 0; i < n; i++){
        if(i < n-1 && value(s[i]) < value(s[i+1])){
            res -= value(s[i]);
        } else {
            res += value(s[i]);
        }
    }

    return res;
}