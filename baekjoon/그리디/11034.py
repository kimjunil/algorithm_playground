# 캥거루 세마리2 (https://www.acmicpc.net/problem/11034)

while True:
    try:
        A,B,C = map(int,input().split())

        d1 = B-A
        d2 = C-B

        print(max(d1, d2)-1)
    except:
        break
