N = int(input())
for i in range(N):
    r,e,c = map(int,input().split())  
    a = e-c # 광고의 순수익
    if a == r: 
        print("does not matter")
    elif a > r: 
        print("advertise")
    else:
        print("do not advertise")