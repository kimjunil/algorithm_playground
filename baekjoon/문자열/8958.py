# OX퀴즈 (https://www.acmicpc.net/problem/8958)

n = int(input())
for _ in range(n):
  quiz = input()
  score = 0
  final_score = 0
  for i in quiz:
    if i=="O":
      score = score + 1
    else:
      score = 0
    final_score = final_score + score
  print(final_score)
