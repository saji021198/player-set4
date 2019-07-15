a1,b=map(int,input().split())

input()

li=list(map(int,input().split()))[:a1]
addli=list(map(int,input().split()))[:b]
result=[]
for i in addli:
    li.append(i)
    print(max(li),end= " ");
