s=input('enter the marks: ').split(',')
p=list(map(int,s[1:]))
print(s[0]," obtained ",sum(p[1:5])," out of 500 in theory and ",sum(p[6:9]),
      " out of 90 in practicals and passed the exam with ",(sum(p[1:])/590)*100," % in aggregate")
