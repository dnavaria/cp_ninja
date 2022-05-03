def isPermutation(string1, string2) :
    if len(string1) != len(string2):
        return False
    freq = {}
    freq2 = {}
    for s in string1:
        freq[s] = freq.get(s,0)+1
    for s in string2:
        freq2[s] = freq2.get(s,0)+1
    for k,v in freq.items():
        if k not in freq2:
            return False
        elif freq[k] != freq2.get(k,-1):
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

