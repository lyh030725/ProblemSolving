 #include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int count = 0;
    for(int num = 1; num <= n; num++){
        int flag = 1;

        if(num/10 < 10){
            count++;
            continue;
        }
        //123
        int copy_num = num;
        int first = copy_num % 10; // 3
        int second = (copy_num / 10)%10; // 2
        copy_num /= 10; //12
        int cur_diff = first-second; // 1
        while(copy_num >= 10){
            int first = copy_num % 10; // 2
            int second = (copy_num / 10)%10;  // 1
            int next_diff = first-second; //1
            copy_num /= 10; // 2
            if(next_diff != cur_diff){
                flag = 0;
                break;
            }
            cur_diff = next_diff;
        }
        if(flag){
            count++;
        }
    }
    printf("%d", count);

    return 0;
}