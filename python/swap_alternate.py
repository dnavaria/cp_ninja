from os import read,fstat
from io import BytesIO

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr):
    for i in range(0,len(arr),2):
        if (i+1)<len(arr):
            arr[i],arr[i+1] = arr[i+1],arr[i]
        else:
            break
    return arr
