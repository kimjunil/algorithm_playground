# 전자레인지(https://www.acmicpc.net/problem/10162)

T = int(input())

if T%10!=0:
  print(-1)
else:
  A = T//(5*60)
  T = T%(5*60)
  B = T//(60)
  T = T%60
  C = T//10

  print(A,B,C)
