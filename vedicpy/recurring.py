from ctypes import CDLL

obj= CDLL("vedicpy/C program files/recurring.so")


def recuring_fractionto_decimal(numerator: int, denominator: int):
    obj.recuring_fractionto_decimal(numerator, denominator)
