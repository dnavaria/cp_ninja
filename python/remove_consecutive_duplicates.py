from sys import stdin


def removeConsecutiveDuplicates(string) :
    ts = ""
    for i in range(1,len(string)):
        if string[i-1] != string[i]:
            ts+=string[i-1]
    return ts+string[-1]



#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
