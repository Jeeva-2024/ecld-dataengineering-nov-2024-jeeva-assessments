def piechart(dic):
    dict={}
    sum_n=0
    for val in dic.values():
        sum_n=sum_n+val
    for key,val in dic.items():
         value=int((val/sum_n)*360)
         dict[key]=value
    return dict
print(piechart({ "a": 30, "b": 15, "c": 55 }))



