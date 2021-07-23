# N X M의 숫자카드에서 각 행별로 가장 작은 수를 찾은 뒤에 서로 비교하여 가장 큰 값을 뽑는 문제
# N,M을 공백으로 구분하여 입력
n, m = map(int,input().split())

result = 0
#한 줄씩 입력뱓아 확인
for i in range(n): # 각 행 별로 데이터를 입력받아 비교한다.
  data = list(map(int,input().split()))
  # 입력받기
  min_value = min(data) # 그 수중에서 가장 작은 값을 min_value에 저장한다.
  result = max(result,min_value)
  # result값과 행에서 뽑은 최솟값이랑 비교하여 더 큰값으로 갱신한다.

  
print(result) #결과 출력
