n=int(input('Enter any Positive integer'))


p=n-2
l=1
for i in range(n):
    if(i==0):
        print(' '*p,'*')
        p-=1
    elif(i==1):
        print(' '*p,'* *')
    elif(i==n-1):
        print('* '*n,end='')
    else:
        p=p-1   
        print(' '*p,'*',' '*l,'*')
        l=l+2
      


