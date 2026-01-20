import heapq

n = int(input())
cards = []
heap = []
for i in range(n):
  data = int(input())
  heapq.heappush(heap, data)

