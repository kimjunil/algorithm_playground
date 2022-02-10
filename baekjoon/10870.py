# 피보나치 수 5 (https://www.acmicpc.net/problem/10870)
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
# n은 20보다 작거나 같은 자연수 또는 0이다.

def fibo(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

print(fibo(int(input())))

# 시간복잡도: O(2^n)
# 공간복잡도: O(2^n)
