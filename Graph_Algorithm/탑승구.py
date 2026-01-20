gate_num = int(input())
airplane_num = int(input())

parent = [0]*(gate_num)
used = [0]*(gate_num)
for i in range(1, gate_num):
  parent[i] = i-1

def find_gate(parent, used, x):
  if(used[x] == 0):
    used[x] = 1
    return True
  else:
    if(parent[x] == x):
      return False
    else:
      return find_gate(parent, used, parent[x])

count = 0
data = []
for i in range(airplane_num):
  data.append(int(input()))
  
for item in data:
  if(find_gate(parent, used, item-1)):
    count += 1
  else:
    break


print(count)