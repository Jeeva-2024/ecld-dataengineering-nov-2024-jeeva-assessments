def pentagonal(n):
    sum=1
    for i in range(1,n):
        sum=sum+(5*i)
    return sum
print(pentagonal(8))