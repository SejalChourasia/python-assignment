s=input('enter the string').split(' ')
n=[int(s[i]) for i in range(2,len(s),3)]
print(sum(n),sum(n)/len(s))

