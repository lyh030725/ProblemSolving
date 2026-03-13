#include <stdio.h>

int trailingZeroes(int n) {
    int count = 0;
    int two_count = 0;
    int five_count = 0;
    for(int i = 2; i <= n; i++){
        int temp = i;
        while(temp % 2 == 0){
            two_count++;
            temp /= 2;
        }
        while(temp % 5 == 0){
            five_count++;
            temp /= 5;
        }
    }
    if(two_count > five_count){
        count = five_count;
    }else{
        count = two_count;
    }

    return count;
}

int main(){
  int n;
  scanf("%d", &n);
  printf("%d", trailingZeroes(n));
  return 0;
}