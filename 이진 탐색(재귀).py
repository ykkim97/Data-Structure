# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array,target,start,end):
    if start > end:
      None
    mid = (start+end) // 2
    # 찾은 경우에는 중간점 인덱스를 반환한다.
    if array[mid] == target:
      return mid
    # 중간점의 값보다 찾고자하는 값이 작은 경우
    elif array[mid] > target:
      return binary_search(array,target,start,mid-1)
    else:
      return binary_search(array,target,mid+1,end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n,target = list(map(int,input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진탐색 수행결과 출력하기
result = binary_search(array,target,0,n-1)
if result == None:
  print('원소가 존재하지 않음')
else:
  print(result+1)
