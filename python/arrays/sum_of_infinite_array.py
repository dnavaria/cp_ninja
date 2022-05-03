mod = 10**9+7

def helper(pref, x, n):
    count = (x // n) % mod
    res = (pref[n] * count) % mod
    return (res + pref[x%n]) % mod

def sumInRanges(arr, n, queries, q):
    ans = []
    # creating an empty prefix array of length n+1
    pref = [0 for i in range(n+1)]
    
    # populating the prefix array with the cummulative sum
    for i in range(1,n+1):
        pref[i] = (pref[i-1] + arr[i-1]) % mod
        
    for l,r in queries:
        # calculating rsum
        rsum = helper(pref,r,n)
        # calculating lsum
        lsum = helper(pref,l-1,n)
        
        ans.append((rsum - lsum)%mod)
    
    return ans