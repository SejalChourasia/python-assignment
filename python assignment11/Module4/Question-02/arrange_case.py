l=list(map(int,input('Enter the Numbers').split(' ')))
d=[0]*(max(l)+1)   
for i in l:
    d[i]=d[i]+1
for j in range(len(d)):
    p=max(d)
    c=d.index(p)
    print(str(c)*p,end='')
    d[c]=0
    if len(d)==0:
        break
