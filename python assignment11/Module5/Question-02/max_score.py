squad={'Batsman': {'yashasvi': {'matches': '5', 'Runs': '90', 'Average': '18', 'Highest': '25'}}, 'Baller': {'Sejal': {'matches': '100', 'Runs': '20', 'Average': '0.2', 'Highest': '2'}}}
m=0
name=''
for i in squad:
    for name in squad[i]:
        for high in squad[i][name]:
            if high=='Highest':
                if (m<int(squad[i][name][high])):
                    m=int(squad[i][name][high])
                    name=squad[i][name]
print('Name of player',name)
print('Score',m)
                    
