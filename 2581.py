# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

def get_prime(n):
  is_prime = [True]*n
  is_prime[0] = False
  
  for i in range(n):
    if is_prime[i]==True:
      for j in range(i+1, n):
        if (j+1)%(i+1)==0:
          is_prime[j] = False
  
  return [i+1 for i, x in enumerate(is_prime) if x==True]

M = int(input())
N = int(input())

prime_num = [x for x in get_prime(N) if x>=M]

if len(prime_num)>0:
  print(sum(prime_num))
  print(min(prime_num))
else:
  print(-1)
