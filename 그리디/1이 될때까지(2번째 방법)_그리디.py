# 1이 될때까지 k로 나누거나 1씩 빼는 문제
# 대상 숫자를 n, 나누는 수를 k라고 하고 입력받는다
n, k = map(int,input().split())
result = 0 # result값 초기화

while True: 
  target = (n // k) * k  # target은 k로 나누어 떨어지는 수
  result +=(n-target) # 원래 n값에서 k로 나누어 떨어지는 수인 target을 뺀 만큼 1씩 빼주기 때문에 횟수를 그 수만큼 result에 추가해준다. 
  n = target
  # n을 target의 값으로 바꿔준다.
  if n < k: # k의 값으로 n을 나누지 못할 때까지 나눠지면 반복문을 빠져나간다.
    break 
  
  result +=1 # 나눈만큼 횟수를 추가해준다.
  n //=k # k로 나눈 몫을 n으로

result +=(n-1) # n을 k로 나누지 못할때 1이 되기 전까지 빼주기때문에 그 횟수만큼 더해준다.
print(result) # 결과 출력
  


