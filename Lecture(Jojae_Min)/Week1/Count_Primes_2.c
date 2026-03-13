#include <stdio.h>
#include <math.h>

int countPrimes(int n){
    int count = 0;
    for (int num = 2; num < n; num++) {
      int flag = 1;
      for (int j = 2; j*j <= num; j++) {
        if(num % j == 0){
            flag = 0;
            break;
        }
      }
      if(flag){
        count++;
      }
    }
    return count;
}

int main(){
    int n;

    scanf("%d", &n);
    
    printf("%d", countPrimes(n));
    return 0;
}