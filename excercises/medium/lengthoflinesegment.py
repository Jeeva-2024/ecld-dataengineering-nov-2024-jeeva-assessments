import math
def linesegment(list1,list2):
    return math.sqrt((list2[0]-list1[0])**2+(list2[1]-list1[1])**2)
print(linesegment([15,7],[22,11]))