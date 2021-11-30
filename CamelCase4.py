import sys

def separate(sentence):
    newText = ""

    for harf in sentence:
        if (harf != harf.lower()):
            newText += " "
        newText += harf

    return newText.split(" ")


def combine(sentence):
    return sentence.split(" ")


def convertCase(words, ind=1):
    newWords = []
    for i in range(len(words)):
        if i >= ind:
            upperWord = words[i][0].upper() + words[i][1:].lower()
            newWords.append(upperWord)
        else:
            newWords.append(words[i].lower())

    return newWords


def final(word):
    sOrC = word[0]
    isMVC = word[2]
    result = ""

    if sOrC == "S":
        strArr = separate(word[4:])
        if isMVC == "V":
            result = convertCase(strArr, len(strArr))
        elif isMVC == "M":
            result = convertCase(strArr, len(strArr))
            result[-1] = result[-1][0: -2]
        elif isMVC == "C":
            result = convertCase(strArr[1:], len(strArr))
        print(" ".join(result))


    elif sOrC == "C":
        strArr = separate(word[4:])
        if isMVC == "V":
            result = convertCase(strArr)
        elif isMVC == "M":
            result = convertCase(strArr)
            result.append("()")

        elif isMVC == "C":
            result = convertCase(strArr, 0)

        print("".join(result))


for line in sys.stdin:
    final(line.replace("\n","").replace("\r",""))

