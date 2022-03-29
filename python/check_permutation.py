def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    freq = {}
    for i in string1:
        if freq.get(i,0) != 0:
            freq[i]+=1
        else:
            freq[i]=1
    for k in string2:
        if freq.get(k,0) == 0:
            return False
    return True


















    




#main
string1 = input()
string2 = input()

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

