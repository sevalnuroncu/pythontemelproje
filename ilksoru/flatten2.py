def flatten(top_l):
    for eleman in top_l:
        if isinstance(eleman,list): #eleman tipi list mi
            yield from flatten(eleman)#return yerine yield kullanmak normal bir fonksiyonu generatöre dönüştürür.
        else:
            yield eleman
l=[[1,'a',['cat'],2],[[[3]], 'dog'],4,5]
flat_list=[a for a in flatten(l)]
print(flat_list)
