def helper(string,index,fstring):
    if index == len(string):
        print(fstring)
        return
    helper(string,index+1,fstring)
    helper(string,index+1,fstring+string[index])

def powerset(string):
    helper(string,0,"")
    return
