# 약수구하기 (https://www.acmicpc.net/problem/2501)
# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오
# 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.
# N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.

N, K = map(int, input().split())

arr = []

for i in range(1, N+1):
  if N%i == 0:
    arr.append(i)
    
if len(arr) < K:
  print(0)
else:
  print(arr[K-1])
  
# 시간복잡도: O(N)
# 공간복잠도: O(N)
