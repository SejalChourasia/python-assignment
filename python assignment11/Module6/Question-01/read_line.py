
infile=open('Hotel.txt','w')
infile.write('Manager'+'\n')
infile.write('Cook')
infile.close()
outfile=open('Hotel.txt','r')
r=outfile.readline()
while r!='':
    print(r.rstrip('\n'))
    r=outfile.readline()
        
outfile.close()
