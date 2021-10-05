# 효율적인 화폐 구성 문제

# N,M 입력받기
n,m = map(int,input().split())

array = [] # 화폐 단위저장
for i in range(n):
  array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 dp테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행
d[0] = 0
for i in range(n):
  for j in range(array[i],m+1):
    if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는경우
      d[j] = min(d[j],d[j-array[i]]+1)

# 계산된 결과 출력

if d[m] == 10001: # 최종적으로 M원을 만들 방법이 없는 경우
  print(-1)
else:
  print(d[m])