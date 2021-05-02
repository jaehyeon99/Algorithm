T = int(input())
for i in range(T):
    R,S = input().split()
    R = int(R)
    S = str(S)
    for j in range(len(S)):
        print(R*S[j], end='')
    print()
    