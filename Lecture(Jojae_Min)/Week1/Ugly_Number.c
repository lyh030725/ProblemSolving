#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#include <stdbool.h>

bool isUgly(int n) {
    // 1. 양의 정수가 아니면, 소인수가 2,3,5일 수 없으므로 false
    if (n <= 0) {
        return false;
    }
    
    // 2. 2, 3, 5로 더 이상 나눌 수 없을 때까지 나눔
    while (n % 2 == 0) n /= 2;
    while (n % 3 == 0) n /= 3;
    while (n % 5 == 0) n /= 5;
    
    // 3. 최종 결과가 1이면 성공
    return n == 1;
}


int main(){
  int n;
  scanf("%d", &n);
  printf("%d",isUgly(n));
  return 0;
}