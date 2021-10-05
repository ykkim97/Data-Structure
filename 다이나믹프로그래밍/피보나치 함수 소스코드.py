# 피보나치 함수를 재귀함수로 구현

def fibo(x):
  if x == 1 or x == 2:
    return 1 # 첫번째와 두번째수는 1이니까
  return fibo(x-1) + fibo(x-2) # 전 수와 전전수를 더한 값을 리턴

print(fibo(4)) # 4번째 피보나치수
