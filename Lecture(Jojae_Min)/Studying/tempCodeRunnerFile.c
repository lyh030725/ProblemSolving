#include <stdio.h>

int main(){
  int fibo[10001] = {0,1};
  int n;
  scanf("%d", &n);

  for(int i = 2; i <= n; i++){
    fibo[i] = fibo[i-1] + fibo[i-2];
  }
  printf("%d", fibo[n]);

  return 0;
}