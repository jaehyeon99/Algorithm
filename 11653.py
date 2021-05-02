n = int(input())
for i in range(2, n):
    if i*i > n: 
        break 
    while n % i == 0:
        print(i)
        n = n //i 
if n > 1:
    print(n)