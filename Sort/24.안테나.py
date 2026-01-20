import sys
input = sys.stdin.readline

n = int(input())

house = list(map(int, input().split()))
length = len(house)

house.sort()
if(length % 2 == 0):
  print(house[length//2-1])
else:
  print(house[length//2])



