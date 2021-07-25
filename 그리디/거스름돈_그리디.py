# 거스름돈을 최소한의 동전 수가 되도록 하려면?
# 그리디 알고리즘으로 해결

# n은 거스름돈, 동전 수를 세기 위한 변수인 count변수 선언 및 초기화
n = 1260
count = 0

# 동전의 종류를 담는 리스트인 coin_types를 초기화해주자.
coin_types = [500,100,50,10]

# coin_types에 대해서 500원 동전부터 반복문을 돌리자. 
for coin in coin_types:
  count = count + n // coin  # 거스름돈을 동전의 종류로 나눠주면 개수가 나옴 -> count 갱신
  n = n % coin # 남은 거스름돈을 갱신해준다.(n을 갱신한다.)

print(count)

