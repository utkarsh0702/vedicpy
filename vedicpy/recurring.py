from ctypes import CDLL
import os

path= os.path.abspath(os.path.join( 'vedicpy', 'vedicpy', 'C program files', 'recurring.so'))
obj= CDLL(path)


def recuring_fractionto_decimal(numerator: int, denominator: int):
    obj.recuring_fractionto_decimal(numerator, denominator)
