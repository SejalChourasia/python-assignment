#writing in the file
out_file=open('Dept.txt','w')
out_file.write('Computer Science'+'\n'+'Mechanical'+'\n'+'Information technology')

out_file.close()

#Reading the File
in_file=open('Dept.txt','r')
c=in_file.read()
print(c.rstrip('\n'))
in_file.close()

# Append
a=open('Dept.txt','a')
a.write('Electronics')
a.close()
