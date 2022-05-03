from sys import stdin

def reverseEachWord(string) :
    fs = ""
    ts = ""
    for i in string:
        if i == " ":
            fs= fs +ts+" "
            ts = ""
        else:
            ts = i+ts
    return fs+ts
#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
