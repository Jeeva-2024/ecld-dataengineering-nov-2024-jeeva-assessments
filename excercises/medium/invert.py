def invert(d):
    dict={}
    for key,value in d.items():
        a=key
        key=value
        value=a
        dict[key]=value
    return dict
print(invert({ "z": "q", "w": "f" }))