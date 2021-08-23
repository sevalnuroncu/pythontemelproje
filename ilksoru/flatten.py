a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_a=[]
for i in a:
    if type(i)==int:
        new_a.append(i)
        a.remove(i)
for i in a:
    if type(i)==int:
        new_a.append(i)
        a.remove(i)
"""print(new_a)
print(a)"""
for i in a:
    for j in i:
        """print(j)"""
        new_a.append(j)
scd_new=[]
"""print(new_a)"""
for i in new_a:
    if type(i)==list:
        scd_new.append(i)
        new_a.remove(i)
trd_new=[]
for i in scd_new:
    for j in i:
        trd_new.append(j)
for i in trd_new:
    if type(i)!=list:
        new_a.append(i)
        trd_new.remove(i)
for i in trd_new:
    for j in i:
        new_a.append(j)
print(new_a)



