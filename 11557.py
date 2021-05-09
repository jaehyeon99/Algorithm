T = int(input())
for i in range(T):  
    N = int(input())
    winner = ''
    max= 0      
    for j in range(N):
        school,num = map(str,input().split()) 
        num = int(num)
        if num > max:
            max = num 
            winner = school
    print(winner)
        
        
    
    