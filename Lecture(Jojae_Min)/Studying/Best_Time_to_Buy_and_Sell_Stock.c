#include <stdio.h>

int main(){

    int prices[] = {7,6,4,3,1};

    int start = prices[0];
    int max = 0;
    for(int i = 1; i < 5; i++){
        int profit = prices[i] - start;
        if(profit < 0){
            start = prices[i];
        }
        else{
            if(profit > max) max = profit;
        }
    }

    printf("%d", max);




    return 0;
}