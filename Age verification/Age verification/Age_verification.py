import datetime


def printWelcomeMsg():
    date = datetime.date(2022, 2, 7)
    msg = "Hi im new and this is my first py program written on {0}".format(date)
    print(msg)


def readUInt():
    value = -1
    while value < 0:
        valueAsString = input("write your age: ")
        if valueAsString.isdecimal():
            value = int(valueAsString)
            break
    return value


def verifyAge():
    print()
    age = readUInt()

    if age < 18:
        print("{0} is minor".format(age))
        return
    if age > 18:
        print("{0} is adult".format(age))
        return
    print("{0} is barely adult".format(age))


printWelcomeMsg()
longMsg = "You and your friends are going to a bar; Input number of friends(imaginary included): "
print(longMsg)
friendsCount = readUInt()
for x in range(friendsCount):
    verifyAge()
