#include <stdio.h>

int trailingZeroes(int n) {
    int count = 0;
    
    // n이 5보다 작아질 때까지 계속 5로 나누면서 몫을 더해줍니다.
    while (n >= 5) {
        count += n / 5;
        n /= 5;
    }
    
    return count;
}


int main(){
  int n;
  scanf("%d", &n);
  printf("%d", trailingZeroes(n));
  return 0;
}