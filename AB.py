X = list(map(int,input().split()))
Max = max(X)
Y = [0]*(Max+1)

for number in X:
    Ynumber]+=1

for number in range(1,Max+1):
    Y[number] += Y[number-1]
    
C = [0] * len(X)
for number in range(len(X)):
    Y[X[number]] -= 1
    X[Y[X[number]]] = X[number]
    
print(C)
