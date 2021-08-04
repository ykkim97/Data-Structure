# 삽입 정렬 코드

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): 
  for j in range(i,0,-1): # 인덱스 i부터 1까지 1씩 감소하며 반복함.
    if array[j] < array[j - 1]: # 이전의 수와 비교하여 더 작은경우 한칸씩 왼쪽으로 이동한다.
      array[j],array[j - 1] = array[j - 1],array[j]
    else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춘다.
      break

print(array)