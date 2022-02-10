# 지능형 기차 2 (https://www.acmicpc.net/problem/2460)
# 10개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.

people_cnt = 0
max_cnt = 0

for _ in range(10):
  OUT, IN = map(int, input().split())
  people_cnt = people_cnt-OUT
  people_cnt = people_cnt+IN
  if people_cnt>max_cnt:
    max_cnt = people_cnt

print(max_cnt)

# 시간복잡도: O(1)
# 공간복잡도: O(1)
