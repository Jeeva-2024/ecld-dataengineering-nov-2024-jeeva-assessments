def area(n,a):
    total_landmass=148_940_000
    propotion=round((a/total_landmass)*100,2)
    return f"{n} is {propotion} of the total worlds landmass"
print(area("russia",17098242))

