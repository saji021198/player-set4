k=int(input())
t=[]
for i in range (2,k+1):
    if(k%i==0 and i%2==0):
        t.append(i)
print(*t)
