#include <stdio.h>

int main(){
  int n;
  scanf("%d", &n);
  int dp[1000] = {1, 2};
  for(int i = 2 ; i < n; ++i){
    dp[i] = (dp[i-1]+dp[i-2])%10007;
  }
  printf("%d", dp[n-1]);

  return 0;
}