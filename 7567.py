height = 10
direction = input()
list(direction)
for i in range(1,len(direction)):
    if direction[i-1] != direction[i]:
        height = height+10
    else:
        height = height+5
print(height)