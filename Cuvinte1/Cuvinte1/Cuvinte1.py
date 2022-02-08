
def isVocal(charr):
    for c in ['a', 'e', 'i', 'o', 'u']:
        if c == charr:
            return True
    return False


def hasStringConsonants(text):
    for charr in text:
        if charr == ' ':
            continue
        if isVocal(charr) == False:
            return True
    return False


textArr = input().split(" ")

for text in textArr:
    if hasStringConsonants(text) == False:
        print(text)
