s = input()

one_count = 0
zero_count = 0

for i in range(1, len(s)):
  if(s[i] != s[i-1] and s[i-1] == "1"):
    one_count += 1
  elif(s[i] != s[i-1] and s[i-1] == "0"):
    zero_count += 1
  if(i == len(s)-1):
    if(s[i] == "0"):
      zero_count += 1
    else:
      one_count += 1

print(min(zero_count,one_count))