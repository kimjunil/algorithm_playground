# 최소, 최대 (https://www.acmicpc.net/problem/10818)
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다

max = -1000000
min = 1000000

N = input()
arr = list(map(int, input().split()))

for i in arr:
  if i<min:
    min = i
  if i>max:
    max = i

print(min, max)

# 시간복잡도: O(N)
# 공간복잡도: O(1)
