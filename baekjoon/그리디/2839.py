# 설탕배달 (https://www.acmicpc.net/problem/2839)

n = int(input())

result = 0
while n>=0:
  if n%5==0:
    result += n//5
    print(result)
    break
  n = n-3
  result += 1
else:
  print(-1)
