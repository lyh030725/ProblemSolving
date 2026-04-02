#include <string.h>
#include <stdio.h>

int lengthOfLongestSubstring(char* s) {
    int left = 0;
    int right = 1;
    int max = 1;
    int length = strlen(s);

    if(length == 0 || length == 1){
        return length;
    }
    int count = 1;
    while(right < length){
        if(s[left] != s[right]){
            count = 2;
            while(right-1 != left){
                left++;
                if(s[left] == s[right]){
                    break;
                }
                count++;
            }
            if(count > max) max = count;
        }
        else{
            left = right;
        }
        right++;
    }
    

    return max;
}

int main(){

    printf("%d", lengthOfLongestSubstring("abcabcbb"));


    return 0;
}