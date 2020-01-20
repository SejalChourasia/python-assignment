n=int(input("Enter the number of packages"))
retail_price=99
if(n>100):
    discount=0.4*n*retail_price
elif(n>50):
    discount=0.3*n*retail_price
elif(n>20):
    discount=0.2*n*retail_price
elif(n>20):
    discount=0.1*n*retail_price
total_amount=retail_price*n-discount
print(discount)
print(total_amount)
