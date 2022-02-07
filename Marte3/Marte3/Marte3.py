def getInput():
    text = input()
    xstr, ystr, nstr = text.split()
    return int(xstr), int(ystr), int(nstr)


x, y, n = getInput()

ani = int(n / (x * y))
anteneRamase = n % (x * y)
zile = int(anteneRamase / y)
ore = anteneRamase % y

print(ani)
print(zile)
print(ore)
