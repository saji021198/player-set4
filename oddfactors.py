p=int(input())
jk=[]
for i in range(1,p+1):
    if(p%i==0 and i%2!=0):
        jk.append(i)
print(*jk)
        
