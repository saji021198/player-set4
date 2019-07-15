k,l=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
y=[]
for i in range (len(q)):
    y.append(q[i])
    print(max(y),end=' ')
