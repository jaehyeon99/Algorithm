n = int(input())
list = [] 
for i in range(n): 
    name, day, month, year = map(str,input().split()) 
    if len(day) == 1:
        day = "0" + day 
    if len(month) == 1:
        month = "0" + month 
    list.append((name, year + month + day))
list = sorted(list, key =lambda x: int(x[1]))
print(list[-1][0])
print(list[0][0])