# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

def get_prime_num(n):
  prime = [True]*n
  prime[0] = False

  for i in range(n):
    if prime[i]==True:
      for j in range(i+1, n):
        if (j+1)%(i+1)==0:
          prime[j] = False

  prime_num = [i+1 for i, x in enumerate(prime) if x==True]
  return prime_num

prime_num = get_prime_num(1000)

N = input()
arr = list(map(int, input().split()))
print(len([x for x in arr if x in prime_num]))
