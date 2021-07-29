# Queue Example
# 큐 예시

# 큐를 구현하기 위해서는 deque라이브러리를 사용한다. (queue 라이브러리보다 deque활용하자.)

from collections import deque

queue = deque()

# 5 2 3 7 순으로 삽입 -> 1개 삭제 -> 1 4순으로 삽입 -> 1개 삭제

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력한다.
queue.reverse() # 다음 출력을 위해 역순으로 바꾼다
print(queue) # 나중에 들어온 원소부터 출력