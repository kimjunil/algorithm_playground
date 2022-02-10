# 문자열 반복 (https://www.acmicpc.net/problem/2675)

N = int(input())

for _ in range(N):
  R, S = input().split()
  for i in range(len(S)):
    for j in range(int(R)):
      print(S[i], end="")
  print("")
