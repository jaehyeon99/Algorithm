T = int(input())
score1 = 100
score2 = 100
for i in range(T):
    player1, player2 = map(int,input().split())  
    if player1 > player2: 
        score2 = score2 -player1 
    elif player1 < player2:
        score1 = score1 -player2 
    else:
        score2 = score2 
        score1 =score1 
print(score1)
print(score2)
        