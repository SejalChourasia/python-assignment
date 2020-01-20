n=int(input("enter the no.of pocket"))
if(n==0):
    print("green")
elif(n>28 and n<=36 or n>10 and n<=18):
    if(n%2==0):
        print("red")
    else:
        print("black")
elif(n>18 or n>0):
    if(n%2==0):
        print("black")
    else:
        print("red")

else:
    print("Invalid no. of pockets entered")
