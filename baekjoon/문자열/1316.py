# 그룹 단어 체커 (https://www.acmicpc.net/problem/1316)

count = 0

N = int(input())
for _ in range(N):
  word = input()
  
  arr = set()
  arr.add(word[0])
  prev_char = word[0]
  for c in word[1:]:
    if prev_char==c:
      continue
    else:
      if c in arr:
        count = count + 1
        break
      else:
        prev_char = c
        arr.add(c)
    
print(N-count)
