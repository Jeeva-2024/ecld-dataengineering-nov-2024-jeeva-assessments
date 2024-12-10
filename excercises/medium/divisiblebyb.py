def divisibleby(a,b):
    if a>b:
        flag=4
        i=a
        while flag>0:
            if(i%b)==0:
               return i
            i=i+1
    else:
        return 0

print(divisibleby(17,8))