from ctypes import CDLL, RTLD_GLOBAL
import os

obj= CDLL(os.path.join(os.getcwd(),'C program files/divisibility.so'), RTLD_GLOBAL)


def divisibility_under10(num: int, divisor: int):
    obj.divisibility_under10(num, divisor)
