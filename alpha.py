p=input()
wq=''
r='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in p:
    if i in r:
        t=r.index(i)
        t=t+3
        wq=wq+r[t]
print(wq)
