# 1이 될때까지 k로 나누거나 1씩 빼는 문제
# 대상 숫자를 n, 나누는 수를 k라고 하고 입력받는다


n, k = map(int,input().split())

result = 0

# N이 K이상이라면 K로 계속 나누기
while n>=k:
  # N이 K로 나누어 떨어지지 않으면 1씩 빼기
  while n % k != 0:
    n = n - 1
    result = result + 1
  # K로 나누기
  n //= k
  result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
  n = n - 1
  result = result + 1

print(result)
