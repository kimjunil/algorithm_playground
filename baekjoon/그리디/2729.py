# 세탁소 사장 동혁 (https://www.acmicpc.net/problem/2720)
for _ in range(int(input())):
    T = int(input())
    Q = T//25
    T = T%25
    D = T//10
    T = T%10
    N = T//5
    T = T%5
    P = T//1
    print(Q, D, N, P)
