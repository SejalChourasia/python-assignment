p=int(input("enter the no. of product"))
i=0
while(i<p):
    w=int(input("enter the wholesale price of item\n"))
    if(w>0):
        r=w*0.5
        print(r)
        i+=1
    else:
        print("re-enter the price with non-negative value")
        
    
    
