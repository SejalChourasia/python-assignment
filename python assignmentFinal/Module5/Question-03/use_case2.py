def carbohydrate():
    m=0
  
    for i in fruits:
        
        for j in fruits[i]:
            if j=='nutrition':
                for k in fruits[i][j]:
                    if k=='Carbohydrate' :
                        if m<float(fruits[i][j][k]):
                            m=float(fruits[i][j][k])
                            name=i
    print('Name of fruit of highest carbohydrate value\n',name)
    print('Carbohydrate',m)
l=[]
def protein_china():
    m=0
    for i in fruits:
       
        for j in fruits[i]:
            if j=='producer':
               
                if 'china' in fruits[i][j]:
                    l.append(i)
            for k in fruits[i][j]:
                if i in l:
                    if k=='protein' :
                        if m<float(fruits[i][j][k]):
                            m=float(fruits[i][j][k])
                            name=i
    print('Name of fruit having highest protein values produced by china\n',name)
    print('Protein',m)
    
                    
            
fruits={'Apple': {'binomial name ': 'malus Domestica', 'producer': ['china', 'unitedState', 'Turkey'], 'nutrition': {'Carbohydrate': '13.81', 'Fat': '0.17', 'protein': '0.4'}}, 'Mango': {'binomial name ': 'mangus', 'producer': ['pakistan', 'india'], 'nutrition': {'Carbohydrate': '14', 'Fat': '0.20', 'protein': '0.13'}},'Orange': {'binomial name ': 'orgus', 'producer': ['china', 'India', 'Turkey'], 'nutrition': {'Carbohydrate': '13.81', 'Fat': '0.17', 'protein': '0.30'}}}
''' fruits={}

n=int(input('Enter the no.of Fruits'))

for i in range(n):
    fruits[input('name of fruit')]={'binomial name ':input('Binomial name'),'producer':input('Enter the major producers').split(' '),'nutrition':{'Carbohydrate':input('Carbohydrate in fruit'),'Fat':input('Fat in fruit'),'protein':input('protein in fruit')}}
    
print(fruits)

'''   
carbohydrate()
protein_china()       
