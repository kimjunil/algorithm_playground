# 일곱 난쟁이 (https://www.acmicpc.net/problem/2309)
# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
# 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다
# (9개의 숫자 중 합이 100이 되는 7개의 수를 찾아라)

arr = [input() for x in 9]
total = sum(arr)

for i in range(len(arr)-1):
  for j in range(i+1, len(arr)):
    a = arr[i]
    b = arr[j]
    if total-(a+b) == 100:
      arr.remove(a)
      arr.remove(b)
      break
  if len(arr)<9:
    break

arr.sort()
print(" ".join(list(map(str, arr))))
