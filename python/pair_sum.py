from os import read,fstat
from io import BytesIO
from collections import defaultdict
def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr,val):
    dd = defaultdict(int)
    pair_count = 0
    for i in range(len(arr)):
        x = arr[i] - val
        if x in dd:
            pair_count+=dd[x]
        dd[arr[i]]+=1
    return pair_count
            

# sol()