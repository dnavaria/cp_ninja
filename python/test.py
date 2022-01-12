from os import read,fstat
from io import BytesIO

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol():
    pass

sol()