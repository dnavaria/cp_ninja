# using xor properties
def xorQuery(queries):
    arr = []
    xor = 0
    for op,val in queries:
        if op == 1:
            arr.append(val^xor)
        elif op == 2:
            xor ^= val
    for i in range(len(arr)):
        arr[i] = arr[i] ^ xor
    return arr

# using prefix array
def sol2(queries):
    # creating a xor prefix array of size 10**5+1
    xorPref = [0] * 10001
    ans = []
    for op,val in queries:
        if op == 1:
            ans.append(val)
        else:
            # here l will always be at 0
            xorPref[0] ^= val
            # but r will change according to the length of the array after insertion
            xorPref[len(ans)] ^= val
            
    for i in range(len(ans)):
        if i == 0:
            ans[i] ^= xorPref[i]
        else:
            # processing the xorPrefix array
            xorPref[i] ^= xorPref[i-1]
            ans[i] ^= xorPref[i]
    return ans