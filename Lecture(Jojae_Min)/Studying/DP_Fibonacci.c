#include <stdio.h>

int main(){
  unsigned long long fibo[10001] = {0,1};
  int n;
  scanf("%d", &n);

  for(int i = 2; i <= n; i++){
    fibo[i] = fibo[i-1] + fibo[i-2];
  }
  printf("%llu", fibo[n]);

  return 0;
}