#include <stdio.h>

int heap[100001];
int size = 0;

void heap_pop(){
  if(size == 0){
    printf("0\n");
    return;
  }
  printf("%d\n", heap[1]);

  heap[1] = heap[size--];
  int parent = 1;
  int child = 2;
  while(child <= size){
    if(child < size && heap[child+1] < heap[child]){
      child++;
    }
    if(heap[parent] <= heap[child]) break;

    int tmp = heap[parent];
    heap[parent] = heap[child];
    heap[child] = tmp;

    parent = child;
    child *= 2;
  }

}

void heap_push(int data){
  heap[++size] = data;
  int copy_size = size;
  while(copy_size != 1 && heap[copy_size/2] > heap[copy_size]){
    int tmp = heap[copy_size];
    heap[copy_size] = heap[copy_size/2];
    heap[copy_size/2] = tmp;
    copy_size /= 2;
  } 
}

int main(){
  int n;
  scanf("%d", &n);

  for(int i = 0; i < n; i++){
    int num = 0;
    scanf("%d", &num);
    if(num == 0){
      heap_pop();
    }
    else{
      heap_push(num);
    }
  }

  return 0;
}