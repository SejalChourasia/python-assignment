import pickle
phonebook={'Yashasvi':'97897989090','Sejal':'543543646','shubhi':'456445547687'}
#write using pickle
outfile=open('phonebook.dat','wb')
pickle.dump(phonebook,outfile)
outfile.close()
#read using pickle
infile=open('phonebook.dat','rb')
r=pickle.load(infile)
infile.close()
print(r)
for i in r:
    print(r[1])
