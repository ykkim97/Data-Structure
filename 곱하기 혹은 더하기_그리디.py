# 곱하기 혹은 더하기
# data라는 문자열을 입력받아 각 자릿수 사이에 곱하기 혹은 더하기만을 넣어 가장 큰수를 만드는 문제이다.
# 연산방향은 일반적인 우선순위를 무시하고 왼쪽에서 오른쪽으로 연산해야한다.
# result는 먼저 기준값을 입력받은 값의 첫번째 수로 초기화한다. 
# 그 다음 수 부터 비교해 나간다.

data = input() # 데이터 입력받기 

result = int(data[0]) # 문자열을 정수형으로 바꾸고 첫번째 자리값을 result로 초기화

for i in range(1,len(data)): # 두번째 자리수 부터 반복하여 비교
  num = int(data[i]) 
  if num <= 1 or result <= 1: # 만약 두 수중에 하나라도 0이나 1(1이하)이면 덧셈한다.
    result += num
  else: # 그게 아니라면 곱해줌
    result *= num

print(result)
 