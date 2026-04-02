#include <string.h>
#include <math.h>

int titleToNumber(char* columnTitle) {
    int length = strlen(columnTitle);
    int res = 0;
    for(int i = length-1; i >= 0; i--){
        res += (columnTitle[i] - 'A' + 1)*(int)pow(26, length-1-i);
    }
    return res;
}