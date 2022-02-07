import datetime


def printWelcomeMsg():
    date = datetime.date(2022, 2, 7)
    msg = "Hi im new and this is my first py program written on {0}".format(date)
    print(msg)


printWelcomeMsg()


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


youAndFriendsCount = 5
for x in range(5):
    verifyAge()
