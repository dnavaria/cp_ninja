from os import read,fstat
from io import BytesIO

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr,target_sum):
    arr = sorted(arr)
    result = []
    n = len(arr)
    i = 0
    while i <= n-3:
        j = i+1
        k = n-1
        while j < k:
            current_sum = arr[i] 
            current_sum += arr[j] 
            current_sum +=  arr[k]
            if current_sum == target_sum:
                result.append([arr[i],arr[j],arr[k]])
                k-=1
                j+=1
            elif current_sum > target_sum:
                k-=1
            else:
                j+=1
        i+=1
    return result
                
            
    

print(sol([1,2,3,4,5,6,7,8,9,15], 18))