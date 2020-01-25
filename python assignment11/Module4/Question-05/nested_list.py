matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print('using append\n',matrix)
m=[[j for j in range(5)] for i in range(5)]
print('Without using append\n',m)
