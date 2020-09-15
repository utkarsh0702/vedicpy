from ctypes import CDLL

obj= CDLL('/home/utkarsh/Desktop/vedicpy/vedicpy/C program files/divisibility.so')


def divisibility_under10(num: int, divisor: int):
    obj.divisibility_under10(num, divisor)
