# 큰 수의 법칙 문제
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 문제
# 연속해서 더해질 수 있는 횟수는 K번
# 수가 같더라도 인덱스가 서로 다르면 다른 수로 취급한다.


n, m, k = map(int,input().split())

data = list(map(int,input().split()))

# 리스트를 정렬해준다.
data.sort()

# 가장 큰 수와 두번째로 큰수만 고르면된다.
# 가장 큰 수를 first라고 두고 두번째로 큰 수는 second라고 둔다.

first = data[n-1]
second = data[n-2]

result = 0 # result는 결과값

while True:
  for i in range(k): # 가장 큰 수를 k번 연속으로 더해준다. 총 덧셈횟수인 m은 1씩 줄여나감.
    if m == 0: # 만약 중간에 m이 0이되면 for문을 break로 빠져나감
      break
    result = result + first # result를 갱신
    m = m - 1 # m을 1씩 줄여준다.

  if m == 0: # 최종적으로 m이 0이면  while문을 빠져나감
    break
  
  result += second 
  # 가장큰수는 k번 반복했기 때문에 두번째로 큰수를 한번 더해주어야 또 가장큰수만 k번 더할 수 있다.
  m = m - 1 # 


print(result)


