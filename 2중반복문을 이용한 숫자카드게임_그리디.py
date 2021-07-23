#N,M을 공백으로 구분하여 입력받기
# 2중 반복문 구조를 이용한 숫자 카드게임
n, m = map(int,input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int,input().split()))
  # 현재 줄에서 가장 작은 수 찾기 
  min_value = 10001
  for a in data:
    min_value = min(min_value,a)
  # 가장 작은 수 들 사이에서 가장 큰 수 찾기  
  result = max(result,min_value)

print(result) 
