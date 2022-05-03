

def reverseStringWordWise(string):
    res = ""
    ts=""
    for i in string:
        ts += i
        if i ==" ":
            res = ts+res
            ts=""
    
    return ts+" " +res
    














    


string = input()
ans = reverseStringWordWise(string)
print(ans)
        
