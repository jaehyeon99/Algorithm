T = int(input())
for i in range(T):
    a = list(input().split())
    num = float(a.pop(0))
    for j in range(len(a)):
        if a[j] == "@":
            num = num * 3
        elif a[j] == "%":
            num = num +5
        elif a[j] == "#":
            num = num -7
    print("%0.2f" %num)