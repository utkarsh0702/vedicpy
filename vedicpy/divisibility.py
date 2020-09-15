from ctypes import CDLL
import os

path= os.path.abspath(os.path.join(  'vedicpy', 'C program files', 'divisibility.so'))
obj= CDLL(path)


def divisibility_under10(num: int, divisor: int):
    obj.divisibility_under10(num, divisor)
