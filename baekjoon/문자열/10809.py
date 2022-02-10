# 알파벳 찾기 (https://www.acmicpc.net/problem/10809)
# 'a' -> 97

word = input()

arr = [-1]*26

for i, c in enumerate(word):
  index = ord(c)-97
  if arr[index] == -1:
    arr[index] = i

print(" ".join(map(str,arr)))
