n=int(input())
i=0
j=0
while(i<n):
    while(j<n):
        if(i==n//2):
            print("*",end=" ")
        elif(j==n//2 and i!=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        
        j=j+1
    print()
    j=0
    i=i+1
    
    
