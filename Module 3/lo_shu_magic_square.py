l=([4,9,2],[3,5,7],[8,1,6])
if(sum(l[0])==sum(l[1])==sum(l[2])==(l[0][0]+l[1][1]+l[2][2])==(l[0][2]+l[1][1]+l[2][0])==(l[0][0]+l[1][0]+l[2][0])==(l[0][1]+l[1][1]+l[2][1])==(l[0][2]+l[1][2]+l[2][2])):
    print("Magic Square")
else:
    print("Not a Magic Square")
