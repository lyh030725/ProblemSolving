//Longest Substring Without Repeating Characters

#include <string.h>

// int lengthOfLongestSubstring(char* s) {
//     int length = strlen(s);

//     if(length == 0 || length == 1){
//         return length;
//     }

//     int left = 0;
//     int right = 1;
//     int max = 1;

//     while(right < length){
//         int copy_left = left;
//         int count = 2;
//         printf("%d %d\n", left, right);

//         if(s[left] != s[right]){
//             int flag = 1;
//             while(copy_left+1 < right){
//                 copy_left++;
//                 if(s[copy_left] == s[right]){
//                     left++;
//                     flag = 0;
//                     break;
//                 }
//                 count++;
//             }
//             if(flag) right++;
//             if(count > max) max = count;
//         }
//         else{
//             left++;
//         }
//         if(right == left){
//             right++;
//         }
//     }
        
    

//     return max;

// }

#include <string.h>

int lengthOfLongestSubstring(char* s){
    int last[256];
    for(int i = 0; i < 256; i++) last[i] = -1;

    int length = strlen(s);
    int left = 0;
    int max= 0;
    //for(int right = 0; s[right]; right++)
    for(int right = 0; right < length; right++){
        if(last[s[right]] >= left){
            left = last[s[right]]+1;
        }
        last[s[right]] = right;
        int len = right-left+1;
        if(len > max) max = len;
    }

    return max;
}
