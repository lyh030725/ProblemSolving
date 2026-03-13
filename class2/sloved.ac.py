import sys
input = sys.stdin.readline

n = int(input())

level = [0]*31

cut = int(n*0.15+0.5)

for i in range(n):
  data = int(input())
  level[data] += 1
  
count = 0
for i in range(1,31):
  if(level[i] >= cut-count):
    level[i] -= cut-count
    break
  else:
    count += level[i]
    level[i] = 0

count = 0
for i in range(30, 0, -1):
  if(level[i] >= cut-count):
    level[i] -= cut-count
    break
  else:
    count += level[i]
    level[i] = 0

count = 0
for i in range(1, 31):
  count += level[i]*i

if(n == 0):
  print(0)
else:
  avg = count/(n-cut*2)
  print(int(avg+0.5))

