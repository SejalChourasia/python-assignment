def insert():
    while(True):
        p=input('What do you wnat to Insert.\nPress 1 To Insert New Building.\nPress 2 Insert New Block.\nPress 3 To Insert In the Block.\nPress 0 to Exit\n')
        if p=='1':
                datastore[input('Enter The Building Name')]={}
        elif p=='2':
                datastore[input('Enter The Building Name')]={input('Enter the block name')}
        elif p=='3':
            
            building=input('Enter The Building Name')
            block=input('Enter the block name')
            
            for i in datastore:
                if i==building:
                    print('hello')
                    for j in datastore[i]:
                        
    
                        if j==block:
                            try:
                                if block=='medical':
                                    
                                    while(True):
                                        print('hello')
                                        datastore[i][j].append({'room_no':input('Enter the Room no.'),'use':input('Enter the use of the Room'),'sq-ft':input('Enter the Area of Room (in sq- feet)'),'price':input('Enter the Price of the Room')})
                                        
                                        ch=int(input('Do You Want to Enter More Rooms.\n Press 1 To Continue .\n Press 0 to Choose Another Option'))
                                        if ch==0:
                                            break
                                elif block=='parking':
                                    datastore[i][j].append({'location':input('Enter the location'),'premium':input('Enter the premium'),'style':input('Enter the style'),'price':input('Enter the Price ')})
                            except e:
                                print(e)
        elif(p=='0'):
            c=input('Press 1 to save the record.\nPress 0 to exit.\n')
            if c=='1':
                try:
                     with open('output.txt','w') as f:
                        for c, v in datastore.items():
                            f.write(c + '\n')
                            f.write("\n".join(["  {}: {}".format(v, d) for v, d in v.items()]) + '\n')
                            f.write('\n')
                except:
                    print('Opps!! some problem occured')
            if c=='0':
                break
             
        
        else:
            print('Please Enter Valid Input')
       
        
        
def Display_Dept():
    
    print('Building and Blocks\n')
    r=open('output.txt','r')
    p=r.readline()
    while p!='':
        print(p)
        p=r.readline()

                    

                                        
datastore={}               
#datastore={'office':{'medical':[{'room_no':100,'use':'reception','sq-ft':50,'price':75},{'room_no':101,'use':'waiting','sq-ft':250,'price':75},{'room_no':102,'use':'examination','sq-ft':290,'price':70},{'room_no':103,'use':'office','sq-ft':300,'price':155}],'parking':[{'location':'premium','style':'covered','price':'750'}]}}


while True:
        
    ch=input('Press 1 to Display\nPress 2 to insert.\nPress 0 to exit\n')
    if ch=='1':Display_Dept()
    elif ch=='2':insert()
  
    elif ch=='0':break
        

