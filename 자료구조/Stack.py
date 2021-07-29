# Stack Example
# 스택 예제

# 5 2 3 7 순으로 삽입후 1개 삭제 이후 1 4 순으로 다시 삽입하고 1개를 다시 삭제한 결과

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])
