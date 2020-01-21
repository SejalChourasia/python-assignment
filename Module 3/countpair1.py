a=list(map(int,input('enter the elements: ')))
sum=int(input('enter the sum'))
c=0
for i in range(len(a)):
    if (sum-a[i]) in a:
        c=1
if(c==1):
    print("yes")
else:
        print("no")
