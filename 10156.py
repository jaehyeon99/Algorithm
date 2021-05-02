K, N, M = map(int,input().split()) 
A = K * N 
B = A - M
if B <= 0:
    print(int(0))
else:
    print(B)
