res= 0
max = 0
for i in range(1,5):
    out, enter = map(int,(input()).split()) 
    res = res - out + enter
    if res > max:
        max = res 
print(max)