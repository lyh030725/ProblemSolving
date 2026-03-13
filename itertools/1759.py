from itertools import combinations
import copy

l, c = map(int, input().split())

data = list(input().split())
first = []
second = []

for i in range(c):
  if(data[i] in ['a', 'e', 'i', 'o', 'u']):
    first.append(data[i])
  else:
    second.append(data[i])

result = []
for i in range(1, l-1):
  cases1 = list(combinations(first, i))
  cases2 = list(combinations(second, l-i))
  for case1 in cases1:
    tmp_list = []
    for value1 in case1:
        tmp_list.append(value1)
    for case2 in cases2:
      copy_list = copy.deepcopy(tmp_list)
      for value2 in case2:
        copy_list.append(value2)
      copy_list.sort()
      result.append(''.join(copy_list))

result.sort()

for res in result:
  print(res)