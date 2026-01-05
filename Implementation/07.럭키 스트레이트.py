n = input()
half = len(n)//2

left_count = 0
right_count = 0
for i in range(len(n)):
  if(i < half):
    left_count += int(n[i])
  else:
    right_count += int(n[i])


if(left_count == right_count):
  print("LUCKY")
else:
  print("READY")