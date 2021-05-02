S = int(input())
sum = 0
for i in range(1, 4294967295):
    sum = sum +i
    if sum > S:
        print(i-1)
        break