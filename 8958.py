T = int(input())
for i in range(T):
    score =0
    num =0 
    ox = list(input())
    for j in range(len(ox)):
        if ox[j] =="O":
            num +=1
            score += num
        elif ox[j] =="X":
            score =score
            num = 0
        
    print(score)
    
