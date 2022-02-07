
# I found the formula for this here https://ecalculator.ro/arie-perimetru-poligon-regulat
# So it actually wouldnt be a hard problem except if you d do this on a test from your memory

import math
p=3.10
print("{0:.2f}".format(p))
print ('%.2f'%p)

def cotangent(A):
    return 1/math.tan(A)

def polygonArea(sides, length):
    if sides < 3:
        return 0.00
    return float(0.25*sides*length*length*cotangent(math.pi/sides))


def readInput():
    var1,var2 = input().split(" ")
    return int(var1),int(var2)

#n,l=readInput()
A = 3.10
Astr= A+""
print(Astr)
formattedA= Astr[0:str(int(A)).__len__()+3]
print(formattedA)
