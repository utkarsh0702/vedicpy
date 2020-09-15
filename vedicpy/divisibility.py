from ctypes import CDLL
import os

obj= CDLL(os.path.abspath(os.path.join(  'vedicpy', 'C program files', 'divisibility.so')))


def divisibility_under10(num: int, divisor: int):
    obj.divisibility_under10(num, divisor)
