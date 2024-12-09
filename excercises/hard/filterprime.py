def filterprime(l):
    lst1=[]
    for val in l:
        for i in range(2,val):
            if(val%i)!=0:
               lst1.append(val)
            break
    return lst1
print(filterprime([2,8,7,11,13]))


