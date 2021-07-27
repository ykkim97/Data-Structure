# 왕실의 나이트 문제
# 8 X 8 좌표평면에서 나이트의 위치가 주어졌을때 나이트가 이동할 수 잇는 경우의 수 출력
# 나이트의 위치를 입력받는다(예를 들어 a2)
# 나이트는 L자 형태로만 이동할 수 있으며 2번이동후 수직으로 한번이동해야한다.
# 공간을 넘어가는경우는 세지 않는다.

# Code
input_data = input()  # 먼저 나이트의 위치를 입력받는다 (첫번째가 알파벳, 두번째가 숫자)
row = int(input_data[1]) # 숫자에 해당하는 부분이 행이므로, input_data[1]
column = int(ord(input_data[0]))-int(ord('a')) + 1 # 알파벳에 해당하는 부분이 열에 해당하고 이를 좌표로 나타내기 위해서 아스키코드로 바꿔주는 함수인 ord()를 이용하여 수로 바꿔준다.

# 나이트가 이동할 수 있는 8가지 방향을 정의한다
steps = [(-2,1),(-1,-2),(1,2),(2,1),(-1,2),(2,-1),(-2,-1),(1,-2)]

# 8가지 방향에 대해서 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  #해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row >= 8 and next_column >= 1 and next_column <= 8:
    result +=1

print(result)