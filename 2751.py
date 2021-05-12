T = int(input())
list = []
for i in range(T):
    a = int(input())
    list.append(a)
list = sorted(list)
for i in range(len(list)):
    print(list[i])