V = int(input()) 
vote = list(input())
countA = 0
countB = 0
for i in range(V):
    if vote[i] == "A":
        countA = countA +1
    else:
        countB = countB +1
if countA > countB:
    print("A")
elif countA < countB:
    print("B")
else:
    print("Tie")