from splitLines import splitLines
from deSpace import deSpace

Tokens = []
Lines = []

file = open(r"C:\Users\theja\Downloads\NOSPOW\test.nospow", "r", encoding="UTF-8")
code = file.read()


Lines = splitLines(code)
print(Lines)
print(splitLines(code))

def tokenize(lines: list, tokensList: list):
    print("Ran")
    cur = ""
    lineIndex = 0
    emptyList = []
    for line in lines:
        tokensList += emptyList
        currentList = tokensList[lineIndex]
        for char in line:
            cur += char
            if cur == "print":
                currentList += cur
                cur = ""
        lineIndex += 1

tokenize(Lines, Tokens)
print(Tokens)