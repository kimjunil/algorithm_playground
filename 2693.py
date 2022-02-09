# 배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.
# 배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

def bubble_sort(arr):
  for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[j] > arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr
        
for i in range(int(input())):
  arr = list(map(int, input().split()))
  print(bubble_sort(arr)[2])
