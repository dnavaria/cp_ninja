from os import read,fstat
from io import BytesIO
from collections import defaultdict

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr1,arr2):
    freq = defaultdict(int)
    
    for el in arr2:
        freq[el] += 1
        
    for el in arr1:
        if el in freq:
            if freq[el] >=1:
                print(el,end=" ")
                freq[el]-=1

# sol()