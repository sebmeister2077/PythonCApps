def printWelcomeMsg():
    msg = "Hi im new"
    print(msg)


printWelcomeMsg()


def verifyAge():
    age = int(input("write your age:"))
    if age < 18:
        print("minor")
    else:
        if age > 18:
            print("adult")
        else:
            print("barely adult")


for x in range(4):
    verifyAge()
