# 뒤집기 (https://www.acmicpc.net/problem/1439)

S = input()

flag = S[0]

a, b = 1, 0
for i in S:
    if i!=flag:
        flag = i
        if flag==S[0]:
            a += 1
        else:
            b += 1
            
print(min(a,b))
