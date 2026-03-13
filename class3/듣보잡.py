import bisect
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list1 = []
list2 = []

for i in range(n):
  list1.append(input().strip())

for i in range(m):
  list2.append(input().strip())

list1.sort()
list2.sort()

def find_str(list, data):
  return bisect.bisect_right(list, data) - bisect.bisect_left(list,data)

result = []
if(n<m):
  for i in range(n):
    data = list1[i]
    if(find_str(list1, data) > 0 and  find_str(list2, data) > 0):
      result.append(data)
else:
  for i in range(m):
    data = list2[i]
    if(find_str(list1, data) > 0 and  find_str(list2, data) > 0):
      result.append(data)

print(len(result))

for res in result:
  print(res)
