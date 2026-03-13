#include <stdio.h>
#include <string.h>

int queue[10000];
int head = -1;
int tail = -1;

void push(int data){
  queue[++tail] = data;
}

void pop(){
  if(head == tail){
    printf("-1\n");
    return;
  }
  printf("%d\n", queue[++head]);
}

void size(){
  printf("%d\n", tail-head);
}

void empty(){
  if(head == tail) printf("1\n");
  else printf("0\n");
}

void front(){
  if(head == tail){
    printf("-1\n");
    return;
  }
  printf("%d\n", queue[head+1]);
}

void back(){
  if(head == tail){
    printf("-1\n");
    return;
  }
  printf("%d\n", queue[tail]);
}

int main(){
  int n;
  scanf("%d", &n);

  for(int i = 0; i < n; i++){
    char command[6];
    int num = 0;
    scanf("%s", command);
    if(strcmp(command, "push") == 0){
      scanf("%d", &num);
      push(num);
    }
    else if(strcmp(command, "pop") == 0){
      pop();
    }
    else if(strcmp(command, "size") == 0){
      size();
    }
    else if(strcmp(command, "empty") == 0){
      empty();
    }
    else if(strcmp(command, "front") == 0) {
      front();
    }
    else{
      back();
    }
  }


  return 0;
} 