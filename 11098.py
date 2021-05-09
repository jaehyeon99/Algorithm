N = int(input())
for i in range(N):
    p = int(input())
    max = 0 
    pick = ''
    for j in range(p):
        num, name = map(str,input().split()) 
        num = int(num)
        if num > max:
            max = num 
            pick = name 
    print(pick)