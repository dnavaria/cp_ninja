from os import read,fstat
from io import BytesIO

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])] >=0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            return abs(arr[i])
    return abs(arr[0])
        

# sol()