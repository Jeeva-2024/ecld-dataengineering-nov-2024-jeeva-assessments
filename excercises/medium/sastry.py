import math
def sastry(n):
    return math.sqrt(int((str(n)+str(n+1)))).is_integer()
print(sastry(106755))