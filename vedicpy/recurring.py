from ctypes import CDLL

obj= CDLL("vedicpy/C program files/recurring.so")


def recuring_fractionto_decimal(num1: int, num2: int):
    obj.recuring_fractionto_decimal(num1, num2)
