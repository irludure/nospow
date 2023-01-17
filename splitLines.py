
def splitLines(code: str):
    allLines = []
    current = ""
    for char in code:
        index = 0
        if char == ";":
            allLines.append(current)
            current = ""
        else:
            current = current + char
            index += 1
        current = current.replace("\n", "")

    return allLines