# 상하좌우이동 문제
# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다.(1<=N<=100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (ex L R U U D D D)

# 출력은 여행가 A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백을 기준으로 출력한다. 최초지점은 (1,1), 공간의 크기는 N X N 크기이다.
# 여행자는 상하좌우로 이동할 수 있으며 계획서의 이동이 공간을 넘어가는 이동이면 그것은 무시되고 다음으로 진행된다. 

# Code
# N 입력받기
n = int(input())
plans = input().split() # 계획서 내용 입력받기
x,y = 1,1 # 여행자의 최초지점 (1,1)초기화
nx,ny = 0,0
# L,R,U,D에 따른 이동 방향을 나타내는 방향벡터 정의하기

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동계획을 하나씩 확인하기
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    #공간을 넘어가는 경우는 무시한다.
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    # 이동 수행
    x,y = nx, ny

print(x,y)

