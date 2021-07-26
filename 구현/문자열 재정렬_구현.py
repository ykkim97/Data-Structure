# 문자열 재정렬
# 입력조건
# 첫째 줄에 하나의 문자열 S가 주어진다.
# 출력조건
# 정답출력하기

# 알파벳을 오름차순으로 정렬하고 그뒤에 숫자들의 합을 붙여서 출력


# Code

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
  if x.isalpha(): # 알파벳인지 확인하고 알파벳은 리스트에 삽입
    result.append(x)
  # 숫자는 따로 더하기
  else: 
    value += int(x)

# 알파벳을 오름차순으로 정렬하기
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입.
if value != 0:
  result.append(str(value))

# 최종결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result)) # 리스트를 문자열로 합쳐서 반환해준다.
