arr = list(map(int,input().split())) 
arr_1 = sorted(arr)
if arr == arr_1:
    print("Good")
else:
    print("Bad")