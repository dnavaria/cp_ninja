def sumInRanges(arr, n, queries, q):
    mx = -1
    for i in queries:
        if i[1] > mx:
            mx = i[1]
    pref = [0]*len(arr)
    for i in range(len(arr)):
        pref[i] = pref[i-1] + arr[i]
    iter = 0
    ans = []
    while q > 0:
        l,r = queries[iter]
        ans.append(pref[r] - pref[l-1])
        iter+=1
        q-=1
    return ans
    
