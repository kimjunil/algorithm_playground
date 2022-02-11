# 제로 (https://www.acmicpc.net/problem/10773)

import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
  i = int(input())
  if i==0:
    stack.pop()
  else:
    stack.append(i)
print(sum(stack))
