n = int(input())
a = list(map(int, input().split()))
a_list = sorted(a, reverse=True)

m = int(input())
b = list(map(int, input().split()))
b_list = sorted(b, reverse=True)

result = []
i = 0
j = 0
count = 0
before_index_a = 0
before_index_b = 0

def start_index(array, length, value, start):
  for i in range(start, length):
    if array[i] == value:
      return i
  return None

while i < n and j < m:
  if a_list[i] == b_list[j]:
    a_index = start_index(a, n, a_list[i], before_index_a)
    b_index = start_index(b, m, b_list[j], before_index_b)
    if a_index == None or b_index == None:
      i += 1
      j += 1
      continue
    if before_index_a > a_index or before_index_b > b_index:
      break
    count += 1
    before_index_a = a_index+1
    before_index_b = b_index+1
    result.append(a_list[i])
    i += 1
    j += 1

  elif a_list[i] > b_list[j]:
    i += 1
  else:
    j += 1

print(count)
for res in result:
  print(res, end = " ")