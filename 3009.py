A,a = map(int,input().split()) 
B,b = map(int,input().split())
C,c = map(int,input().split()) 
if A==B: 
    D = C
    
elif A==C: 
    D = B
elif B ==C:
    D = A
if a==b: 
    d = c
    
elif a==c: 
    d = b
elif b ==c:
    d = a
print(D,d)