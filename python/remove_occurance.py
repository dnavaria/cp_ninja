def removeAllOccurrencesOfChar(string,c):
    fs = ""
    for i in string:
        if i == c:
            continue
        fs+=i
    return fs
    


string = input()
c = input()
output = removeAllOccurrencesOfChar(string,c)
print(output)
