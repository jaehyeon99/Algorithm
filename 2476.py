N = int(input())
result = 0
max_result = 0 
for i in range(N):
    a,b,c = map(int,input().split())
    if a == b == c:
        result = 10000+(1000*a)
    elif a == b or a == c:
        result = 1000+ (a*100)
    elif b == c:
        result = 1000 + (b*100)
    else:
        result = max(a,b,c) *100
    
    if result>max_result:
        max_result = result
        
print(max_result)