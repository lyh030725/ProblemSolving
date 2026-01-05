data = input()

num_count = 0
words = []

for word in data:
  if("0" <= word <= "9"):
    num_count += int(word)
  else:
    words.append(word)

words.sort()

if(num_count != 0):
  words.append(str(num_count))


print(''.join(words))