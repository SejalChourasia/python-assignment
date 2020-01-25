n=int(input('Enter any Positive integer'))
p=0
m=n-2
for i in range(n):
    for j in range(n):
        if(j>=n//2-i and j<=n//2+i and i<n//2):
            print('*',end='')
        elif(i==n//2):
            print('*',end='')
        
        elif(i>n//2):
            
            print(' '*p , '*'*m,' '*p,end='\n')
            p=p+1
            m=m-2
            
        else:
           print(' ',end='')
        
    print()
       
