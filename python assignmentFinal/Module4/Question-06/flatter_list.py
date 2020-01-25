l=[[int(i) for i in range(10)]for j in range(10)]
print('Unflattened list',l)
flatten=[i  for sublist in l for i in sublist if i<5]
'''
for sublist in l:
    for i in sublist:
        flatten.append(i)
'''
print('flattened list with less than 5 ',flatten)
