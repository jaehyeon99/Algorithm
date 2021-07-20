N = int(input())
num = N #26
count = 0

while True:
    a = num //10 # 2
    b = num % 10 #6
    c = (a+b) % 10
    num = (b*10) + c    
    count = count +1
    if(num == N):
        break
print(count)