A,B,C= map(int,input().split())
if B >= C:
    print(-1)
else:
    N= A/(C-B)
    print(int(N)+1)