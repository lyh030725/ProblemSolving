//찾기

#include <stdio.h>
#include <string.h>

int t[1000000];
char text[1000001];
char pattern[1000001];
int index_arr[1000000];

int main(){

    gets(text);
    gets(pattern);

    int n = strlen(text);
    int m = strlen(pattern);

    int j = 0;
    for(int i = 1; i < m; i++){
        while(j > 0 && pattern[i] != pattern[j]) j = t[j-1];
        if(pattern[i] == pattern[j]) t[i] = ++j;
    }

    int i = 0;
    j = 0;
    int count = 0;
    
    while(n-i >= m-j){
        if(text[i] == pattern[j]){
            i++;
            j++;
        }
        else{
            if(j > 0){
                j = t[j-1];
            }
            else{
                i++;
            }
        }
        if(j == m){
            index_arr[count++] = i-m+1;
            j = t[j-1];
        }
    }

    printf("%d\n", count);

    for(int i = 0; i < count; i++){
        if(i == count-1){
            printf("%d", index_arr[i]);
            break;
        }
        printf("%d ", index_arr[i]);
    }

    return 0;
}