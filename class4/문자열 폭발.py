data = input().rstrip()
bomb = input().rstrip()
m = len(bomb)

stack = []

for ch in data:
    stack.append(ch)
    
    # 마지막 글자가 bomb의 마지막 글자와 같을 때만 검사
    if ch == bomb[-1] and len(stack) >= m:
        if ''.join(stack[-m:]) == bomb:
            del stack[-m:]

result = ''.join(stack)

print(result if result else "FRULA")
