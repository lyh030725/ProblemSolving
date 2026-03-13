result = 0
for i in range(3):
  data = input()
  if(data != "Fizz" and data != "Buzz" and data != "FizzBuzz"):
    result = int(data) + 3-i

if(result % 3 == 0 and result % 5 == 0):
  print("FizzBuzz")
elif(result % 3 == 0):
  print("Fizz")
elif(result % 5 == 0):
  print("Buzz")
else:
  print(result)
