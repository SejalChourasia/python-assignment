def countPair():
    a=list(map(int,input('enter the elements: ')))
    b=list(map(int,input('enter the elements: ')))
    x=int(input('enter the sum'))
    c=0
    for i in range(len(a)):
        if (x-a[i]) in b:
            c=c+b.count(x-a[i])
    print(c)
countPair()
