T = int(input())
A=int(0)
B=int(0)
C=int(0)
if T %10 != 0:
    print(-1)
else: 
    A = T // 300 
    T = T -(A*300) 
    B = T // 60
    T = T -(B*60)
    C = T // 10  
    print(A, B, C)