def subArrayCount(arr, k):
    # Return count of all the subarray that have sum is divisible by 'k'.
    # pref = [sum(arr[:i+1]) for i in range(len(arr))]
    # for i in range(len)
    rem_map = {}
    rem_map[0] = 1
    count = 0
    sums = 0
    for i in range(len(arr)):
        sums+=arr[i]
        rem = sums%k
        if rem in rem_map:
            count+=rem_map[rem]
            rem_map[rem]+=1
        else:
            rem_map[rem]=1
    return count