#include <stdio.h>
#include <string.h>

int main() {
    char str[51];
    scanf("%s", str);

    int sum = 0;
    int num = 0;
    int isMinus = 0;  // '-' 등장 여부

    for (int i = 0; i <= strlen(str); i++) {
        if (str[i] == '+' || str[i] == '-' || str[i] == '\0') {
            if (isMinus) {
                sum -= num;
            } else {
                sum += num;
            }

            num = 0;

            if (str[i] == '-') {
                isMinus = 1;
            }
        } 
        else {
            num = num * 10 + (str[i] - '0');
        }
    }

    printf("%d\n", sum);
    return 0;
}