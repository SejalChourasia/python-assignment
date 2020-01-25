people={1:{'name':'Yashasvi','age':'19'},2:{'name':'Sejal','age':'20'}}
print(people)
print(people[1]['name'])
people[3]={}
people[3]['name']='Luna'
people[3]['age']='27'
people[1]['sex']=people[2]['sex']=people[3]['sex']='Female'
print(people[3])
people[4]={'name':'shubh','age':'30','sex':'male'}
print(people[4])
del people[4]['age']
print(people[4])
for p_id,p_info in people.items():
    print('Person id',p_id)
    for key in p_info:
        print(key+':'+p_info[key])
