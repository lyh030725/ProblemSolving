n = int(input())
people = list(map(int , input().split()))
people.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹 내의 인원 수

for i in people:
  count += 1
  if count >= i:
    result += 1
    count = 0


print(result)
