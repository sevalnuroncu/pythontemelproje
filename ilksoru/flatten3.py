def inside_loop(input_list):
    for item in input_list:
        if type(item)!=list:
            flatten_list.append(item)
            #print(flatten_list)
        else:
            inside_loop(item)

flatten_list=[]
inside_loop([[1,'a',['cat'],2],[[[3]], 'dog'],4,5])
print(flatten_list)
