T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    x = A  
    y = B 
    while B != 0:
        r = A%B
        A = B 
        B = r 
    gcd = A
    lcd = x*y /A 
    print(int(lcd))