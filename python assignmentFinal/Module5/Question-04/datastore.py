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
                    for j in datastore[i]:
                        if j==block:
                            if block=='medical':
                                while(True):
                                    datastore[i][j].append({'room_no':input('Enter the Room no.'),'use':input('Enter the use of the Room'),'sq-ft':input('Enter the Area of Room (in sq- feet)'),'price':input('Enter the Price of the Room')})
                              
                                    ch=int(input('Do You Want to Enter More Rooms.\n Press 1 To Continue .\n Press 0 to Choose Another Option'))
                                    if ch==0:
                                        break
                            elif block=='parking':
                                 datastore[i][j].append({'location':input('Enter the location'),'premium':input('Enter the premium'),'style':input('Enter the style'),'price':input('Enter the Price ')})
         
        elif(p=='0'):
            break
        else:
            print('Please Enter Valid Input')
def Display_Dept():
    
    print('No. of Deptmenents \n')
    for i in datastore:
        print(i,end='')
        for j in datastore[i]:
            print(' '*15,j,end='')
        print()
    ch=input('Enter the Block name to view.\n Press 0 to exit')
    if ch==0:
        return
    else:
        for i in datastore:
            for j in datastore[i]:
                if j==ch:
                    l=[i  for i in datastore[i][j][0]]
                    #print(l)
                    for m in range(len(l)):
                                   
                        print(l[m],' '*15,end='' )
                    print()
                    for x in range(len(l)):
                        for k in l:
                        
                        
                            print(datastore[i][j][x][k],' '*15,end=' ')
                        print()
                        
                    print()
                    
                    
def Update():
    while(True):
        building=input('Enter The Building Name in which You want to Update.\n')
        block=input('Enter the block name in which You want to Update.\n')
        Area=input('Enter the Area in the Block Which You Want To Update.\n')
        #ch=input('Press 0 to Exit\n')
        for i in datastore:
                if i==building:
                    print(i)
                    for j in datastore[i]:
                        if j==block:
                            print(j)
                            o=int(input('Select the Area\n'))
                            for  k  in range(len(datastore[i][j])):
                               
                                if (k)==(o-1):
                                    for x in [l  for l in datastore[i][j][k]]:
                                        if x==Area:
                                            print(i,j,k)
                                            datastore[i][j][k][x]=input('Enter the New Value.\n')
                
datastore={'office':{'medical':[{'room_no':100,'use':'reception','sq-ft':50,'price':75},{'room_no':101,'use':'waiting','sq-ft':250,'price':75},{'room_no':102,'use':'examination','sq-ft':290,'price':70},{'room_no':103,'use':'office','sq-ft':300,'price':155}],'parking':[{'location':'premium','style':'covered','price':'750'}]}}

while True:
        
    ch=input('Press 1 to Display\nPress 2 to insert.\nPress 3 to update\nPress 0 to exit\n')
    if ch=='1':Display_Dept()
    elif ch=='2':room()
    elif ch=='3':Update()
    if ch=='0':break
            

