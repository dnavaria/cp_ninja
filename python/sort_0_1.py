from os import read,fstat
from io import BytesIO

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr):
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i] == 1 and arr[j] == 0:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        elif arr[i] == 1 and arr[j] == 1:
            j-=1
        else:
            i+=1

# sol()