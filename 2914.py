import math
A,I = map(int,input().split()) # 38 24
X = (I-1)+0.01  # 23.01
print(math.ceil(X*A))