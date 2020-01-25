

# write
a=open('College.txt','wb')
a.write(b'electronics')
a.close()
#Reading the File
in_file=open('College.txt','rb')
c=in_file.read()
print(c)
in_file.close()
#Append
a=open('College.txt','ab')
a.write(b'Agriculture')
a.close()

#Read and Write
a=open('College.txt','r+b')
a.write(b'Chemical')
a.close()


