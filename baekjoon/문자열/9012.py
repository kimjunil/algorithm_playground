# 괄호 (https://www.acmicpc.net/problem/9012)

for _ in range(int(input())):
  s = input()
  
  q = []
  for i in range(len(s)):
    if s[i]=="(":
      q.append(s[i])
    else:
      if len(q)==0:
        print("NO")
        q.append(s[i])
        break
      else:
        q.pop()
  
  if len(q)==0:
    print("YES")
  else:
    print("NO")
