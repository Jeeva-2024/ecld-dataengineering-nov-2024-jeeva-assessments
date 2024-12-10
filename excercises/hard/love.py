def love(n):
    lst=[]
    for i in range(1,n+1):
        if(i!=n):
            if(i%2==0):
                lst.append("loves me not")
            else:
                lst.append("loves me")

        else :
            if (i % 2 == 0):
                lst.append("LOVES ME NOT")
                final=", ".join(lst)
                return final
            else:
                lst.append("LOVES ME")
                final = ", ". join(lst)
                return final

print(love(4))








