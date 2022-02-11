# 수 찾기 (https://www.acmicpc.net/problem/1920)

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

m_map = {x:0 for x in n_list}
for i in m_list:
    if m_map.get(i)==None:
        print(0)
    else:
        print(1)
