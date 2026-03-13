#include <stdio.h>
#include <string.h>

int stack[10000];
int top = -1;

void push(int data){
  top++;
  stack[top] = data;
}

void pop(){
  if(top == -1){
    printf("-1\n");
    return;
  }
  printf("%d\n", stack[top]);
  top--;
}

void size(){
  printf("%d\n", top+1);
}

void empty(){
  if(top == -1) printf("1\n");
  else printf("0\n");
}

void top_func(){
  if(top == -1){
    printf("-1\n");
    return;
  }
  printf("%d\n", stack[top]);
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
    else{
      top_func();
    }
  }


  return 0;
}