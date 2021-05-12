N = int(input())
res_1 = 0
res_2 = 1
for i in range(N):
    temp = res_2
    res_2 = res_1+res_2
    res_1 = temp
print(res_1)